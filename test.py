from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
# Apply any customizations you did during training
# For example, tokenizer.add_tokens(['new_token1', 'new_token2'])

tokenizer.save_pretrained("./GPT2-FineTuned")

