import re

def clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Remove unwanted characters, this regex can be customized
        text = re.sub(r'[^A-Za-z0-9.,!?()\'\";:]+', ' ', text)
    return text

cleaned_text = clean_text('combined_books.txt')

with open('cleaned_combined_books.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

