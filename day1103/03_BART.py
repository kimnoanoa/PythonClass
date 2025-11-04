import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration

model_name = "gogamza/kobart-summarization"

tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

print("요약/설명 모드입니다. 'exit' 입력시 종료.")

while True:
    user_text = input("\n긴 텍스트 붙여넣기:")
    if user_text.strip().lower() in ['exit', 'quit']:
        break

    raw_ids = tokenizer.encode(user_text)
    input_ids = [tokenizer.bos_token_id] + raw_ids + [tokenizer.eos_token_id]

    input_tensor = torch.tensor([input_ids])

    summary_ids = model.generate(
        input_tensor,
        max_length=128,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3
    )

    answer = tokenizer.decode(summary_ids[0].tolist(), skip_special_tokens=True)
    print("응답:", answer)