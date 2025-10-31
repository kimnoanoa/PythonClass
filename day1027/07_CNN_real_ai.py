import os, numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# ====================
# 설정 - os.path.join() 자동으로 현재 os에 맞는 구분자를 사용
# full대문자 - 상수 네이밍 (바꾸지 않겠다, 고정 파라미터)
# ====================

BASE_DIR    = "real_ai"  
TRAIN_DIR   = os.path.join(BASE_DIR, "train")
TEST_DIR    = os.path.join(BASE_DIR, "test")
TRAIN_CSV   = os.path.join(BASE_DIR, "train.csv")
TEST_CSV    = os.path.join(BASE_DIR, "test.csv")

IMG_SIZE    = 128       # 이미지 사이즈 128 x 128로 통일
CHANNELS    = 3         # 사진: 3채널(RGB)
BATCH_SIZE  = 64
EPOCHS      = 20
SEED        = 42

# ====================
# 이미지 -> 배열 함수
# ====================
def load_image_as_array(path, img_size=IMG_SIZE, channels=CHANNELS):
    img = tf.keras.utils.load_img(path, target_size=(img_size, img_size),
                                  color_mode="rgb" if channels==3 else "grayscale")
    # Pillow Image 객체 반환
    arr = tf.keras.utils.img_to_array(img)
    # 이미지 배열 반환 (128, 128, 3)
    arr = arr / 255.0
    return arr

# ====================
# 경로 컬럼 추가 함수
# ====================
def load_split_data():
    df = pd.read_csv(TRAIN_CSV) # columns: Image, Label (0/1)
    '''
    Image   Label
    1.jpg     0
    2.jpg     0
    '''
    # 경로 붙이기
    df['path'] = df['Image'].apply(lambda x: os.path.join(TRAIN_DIR, str(x)))
    '''
    Image   Label           path
    1.jpg     0         real_ai/train/1.jpg
    2.jpg     0         real_ai/train/2.jpg
    '''

    # stratify 분할 (클래스 비율 유지 - 데이터 불균형 방지)
    tr_df, va_df = train_test_split(df, test_size=0.2, random_state=SEED, stratify=df["Label"])

    # 리스트컴프리헨션으로 로딩
    X_train = np.stack([load_image_as_array(p) for p in tr_df['path'].values])
    y_train = tr_df["Label"].values.astype("float32") 

    print('\n----- X_train.shape: ', X_train.shape)
    print('\n----- y_train.shape: ', y_train.shape)

    X_val = np.stack([load_image_as_array(p) for p in va_df['path'].values])
    y_val = va_df["Label"].values.astype("float32") 

    return (X_train, y_train), (X_val, y_val)

# ====================
# CNN 모델 빌드
# ====================