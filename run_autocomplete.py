from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "./GPT2-FineTuned"  # Path where you saved your model
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
# tokenizer.save_pretrained("./GPT2-FineTuned")


def generate_text(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

prompt = input("enter the text: ")
generated_text = generate_text(prompt)
print(generated_text, "+++++++")
