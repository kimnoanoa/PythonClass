import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Model

#=================================
# 0. 설정값
#=================================

LATENT_DIM = 256    # 순환층 셀 개수 256
BATCH_SIZE = 32     # 32개씩 넣으며 파라미터 업데이트
EPOCHS = 50         # 전체 데이터를 50번 반복
MAX_LEN = 60        # 문장 최대 길이 (문자 개수)

SOS_TOKEN = "<" # start of sequence (decoder 시작)
EOS_TOKEN = ">" # end of sequence   (decoder 종료)
UNK_TOKEN = "U"
PAD_ID = 0          # 패딩 인덱스

DATA_PATH = "polite_pairs.txt"

#=================================
# 1. 데이터 불러오기 (탭으로 구분)
#=================================

src_texts = []
tgt_texts = []

with open(DATA_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip() # 앞뒤 공백, 라인개행 제거
        if not line:
            continue
        parts = line.split("\t") # Q, A 를 나눠서 리스트로
        # parts = ['지금 뭐하고 계세요?', '지금 뭐해?']
        if len(parts) != 2:
            continue
        src, tgt = parts # 리스트 언패킹 (순서대로 할당)
        src_texts.append(src)
        tgt_texts.append(tgt)

print("샘플 개수:", len(src_texts))
print("예시:", src_texts[0], "->", tgt_texts[0])

#=================================
# 2. 문자 사전 만들기
#=================================

input_chars = set()
target_chars = set()

# for s in src_texts:
#     for ch in s:
#         input_chars.add(ch)

# for t in tgt_texts:
#     for ch in t:
#         target_chars.add(ch)

for s in src_texts:
    for w in s.split():
        input_chars.add(w)

for t in tgt_texts:
    for w in t.split():
        target_chars.add(w)

target_chars.add(SOS_TOKEN)
target_chars.add(EOS_TOKEN)
input_chars.add(UNK_TOKEN)
target_chars.add(UNK_TOKEN)

# 정렬해서 인덱스 고정
input_chars = sorted(list(input_chars))
target_chars = sorted(list(target_chars))

# 인덱스 매핑
input_char2idx = {ch:i+1 for i,ch in enumerate(input_chars)}
target_char2idx = {ch:i+1 for i,ch in enumerate(target_chars)}
print('\ninput_char2idx')
print(list(input_char2idx.items())[:20])
print('\ntarget_char2idx')
print(list(target_char2idx.items())[:20])

# 역매핑
input_idx2char = {i:c for c,i in input_char2idx.items()}
target_idx2char = {i:c for c,i in target_char2idx.items()}
print('\ninput_idx2char')
print(list(input_idx2char.items())[:15])
print('\ntarget_idx2char')
print(list(target_idx2char.items())[:15])

num_encoder_tokens = len(input_char2idx) + 1  # +1 for pad(0)
num_decoder_tokens = len(target_char2idx) + 1 

print('\nnum_encoder_tokens:', num_encoder_tokens)
print('num_decoder_tokens:', num_decoder_tokens)

#=================================
# 3. 시퀀스 숫자화 & 패딩 함수
#=================================

# 문장을 숫자로 (정수 레이블링)
# def text_to_ids(text, char2idx, add_sos=False, add_eos=False):
#     ids = []
#     if add_sos:
#         ids.append(char2idx[SOS_TOKEN])
#     for ch in text:
#         ids.append(char2idx[ch])
#     if add_eos:
#         ids.append(char2idx[EOS_TOKEN])
#     # 패딩
#     if len(ids) < MAX_LEN:
#         ids = ids + [PAD_ID] * (MAX_LEN - len(ids))
#     else:
#         ids = ids[:MAX_LEN]
#     return ids

def text_to_ids(text, char2idx, add_sos=False, add_eos=False):
    ids = []
    if add_sos:
        ids.append(char2idx[SOS_TOKEN])
    for w in text.split():
        if w in char2idx:
            ids.append(char2idx[w])
    if add_eos:
        ids.append(char2idx[EOS_TOKEN])
    # 패딩
    if len(ids) < MAX_LEN:
        ids = ids + [PAD_ID] * (MAX_LEN - len(ids))
    else:
        ids = ids[:MAX_LEN]
    return ids

encoder_input_data = []
decoder_input_data = []
decoder_target_data = []

# 위 함수를 이용하여 인코더입력/디코더입력/디코더정답 문장을 숫자로
for src, tgt in zip(src_texts, tgt_texts):
    # 인코더 입력: 존댓말 문장 전체 + pad
    enc_ids = text_to_ids(src, input_char2idx, add_sos=False, add_eos=False)

    # 디코더 입력: SOS + 반말
    dec_in_ids = text_to_ids(tgt, target_char2idx, add_sos=True, add_eos=False)

    # 디코더 정답: 반말 + EOS
    dec_out_ids = text_to_ids(tgt, target_char2idx, add_sos=False, add_eos=True)

    encoder_input_data.append(enc_ids)
    decoder_input_data.append(dec_in_ids)
    decoder_target_data.append(dec_out_ids)

encoder_input_data = np.array(encoder_input_data, dtype=np.int32)
decoder_input_data = np.array(decoder_input_data, dtype=np.int32)
decoder_target_data = np.array(decoder_target_data, dtype=np.int32)
decoder_target_data = np.expand_dims(decoder_target_data, -1)
# saprse_categorical_crossentropy는 마지막 차원에 인덱스가 들어있는 3D 형태를 기대.

# =================================== 데이터 준비 끝!!! ===================================


#=================================
# 4. 인코더-디코더 모델 정의
#=================================

# 인코더
encoder_inputs = layers.Input(shape=(MAX_LEN,), name="encoder_input")
enc_emb = layers.Embedding(
    input_dim=num_encoder_tokens,
    output_dim=128,
    mask_zero=True, # 패딩(0번 인덱스)을 무시
    name="enc_embedding"
)(encoder_inputs)

encoder_lstm = layers.LSTM(
    LATENT_DIM, # 셀 개수
    return_state=True, # 마지막 상태(h,c) 반환
    name="encoder_lstm"
)

# 아웃풋, 은닉상태, 셀상태
_, state_h, state_c = encoder_lstm(enc_emb)
encoder_states = [state_h, state_c] # 마지막 은닉상태, 셀상태


# 디코더
decoder_inputs = layers.Input(shape=(MAX_LEN,), name="decoder_input")
dec_emb = layers.Embedding(
    input_dim=num_decoder_tokens,
    output_dim=128,
    mask_zero=True,
    name="dec_embedding"
)(decoder_inputs)

decoder_lstm = layers.LSTM(
    LATENT_DIM, #256
    return_sequences=True, # 타임스탭마다 출력
    return_state=True, # 마지막 상태 따로 반환(h, c)
    name="decoder_lstm"
)
decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
# 이니셜 스테이트 - 초기 은닉상태

decoder_dense = layers.Dense(
    num_decoder_tokens,
    activation="softmax",
    name="decoder_dense"
)
decoder_outputs = decoder_dense(decoder_outputs)

# 훈련 모델
# 왼쪽에는 시작하는 층, 오른쪽에는 끝나는 값
train_model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
train_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print(train_model.summary())

train_model.fit(
    [encoder_input_data, decoder_input_data],
    decoder_target_data,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    verbose=1
)

#=================================
# 5. 추론용 모델 분리
#=================================

# 인코더 추론 모델
encoder_model = Model(encoder_inputs, encoder_states)

# 디코더 추론 입력들
dec_state_input_h = layers.Input(shape=(LATENT_DIM,), name="dec_state_h_in")
dec_state_input_c = layers.Input(shape=(LATENT_DIM,), name="dec_state_c_in")
dec_single_input = layers.Input(shape=(1,), name="dec_single_token")

# 학습된 레이어 재사용 ()
dec_emb_layer = train_model.get_layer("dec_embedding")
dec_lstm_layer = train_model.get_layer("decoder_lstm")
dec_dense_layer = train_model.get_layer("decoder_dense")

dec_single_emb = dec_emb_layer(dec_single_input)
dec_outputs_step, h_new, c_new = dec_lstm_layer(
    dec_single_emb,
    initial_state=[dec_state_input_h, dec_state_input_c]
)
dec_probs = dec_dense_layer(dec_outputs_step)

decoder_model = Model(
    [dec_single_input, dec_state_input_h, dec_state_input_c],
    [dec_probs, h_new, c_new]
)

#=================================
# 6. 디코딩 함수
#=================================

sos_id = target_char2idx[SOS_TOKEN]
eos_id = target_char2idx[EOS_TOKEN]

print('\n<SOS>:', sos_id, ' ', '<EOS>:', eos_id)

# 정수화 및 패딩
def encode_src(sentence):
    # ids = []
    # for ch in sentence:
    #     if ch in input_char2idx:
    #         ids.append(input_char2idx[ch])
    #     else:
    #         ids.append(input_char2idx["U"])
    ids = [input_char2idx[w] for w in sentence.split() if w in input_char2idx]

    if len(ids) < MAX_LEN:
        ids = ids + [PAD_ID]*(MAX_LEN-len(ids))
    else:
        ids = ids[:MAX_LEN]
    return np.array([ids], dtype=np.int32)

def greedy_decode(input_sentence, max_len=60):
    # 인코더로 state(h,c) 추출
    enc_arr = encode_src(input_sentence)
    h, c = encoder_model.predict(enc_arr, verbose=0)

    # 디코더 시작 토큰 sos_id
    target_seq = np.array([[sos_id]], dtype=np.int32)

    decoded_ids = []

    for _ in range(max_len):
        probs, h, c = decoder_model.predict([target_seq, h, c], verbose=0)
        token_id = np.argmax(probs[0, -1, :])

        if token_id == eos_id:
            break

        decoded_ids.append(token_id)
        target_seq = np.array([[token_id]], dtype=np.int32)

    out_chars = []
    for tid in decoded_ids:
        if tid == 0: # 패딩은 무시해라
            continue
        if tid == input_char2idx["U"]:
            continue
        ch = target_idx2char.get(tid, "")
        out_chars.append(ch)

    return " ".join(out_chars)



#=================================
# 7. 테스트
#=================================

test_sentences = [
    "지금 뭐 하고 계세요?",
    "몸은 좀 괜찮으세요?",
    "늦어서 죄송합니다.",
    "걱정하지 마세요.",
    "내일 시간 되세요?",
    "천천히 오셔도 됩니다.",
    "청주 날씨는 어때요?",
    "도와주셔서 감사합니다.",
    "오늘 기분은 어떠세요?"
]

for s in test_sentences:
    print("INPUT :", s)
    print("OUTPUT :", greedy_decode(s))
    print("-----")