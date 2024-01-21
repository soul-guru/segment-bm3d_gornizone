from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')

set_seed(42)

gen = generator("a want to ", max_length=30, num_return_sequences=5)

for i in gen:
    print(i)
