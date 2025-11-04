import tensorflow as tf
from transformers import AutoTokenizer
from transformers import TFGPT2LMHeadModel

model = TFGPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2', from_pt=True)
tokenizer = AutoTokenizer.from_pretrained('skt/kogpt2-base-v2')

sent = '임진왜란이란'

input_ids = tokenizer.encode(sent)
input_ids = tf.convert_to_tensor([input_ids])
print(input_ids)

output = model.generate(input_ids,
                        max_length=128,
                        repetition_penalty=2.0,
                        use_cache=True)
output_ids = output.numpy().tolist()[0]
print(output_ids)

print(tokenizer.decode(output_ids))