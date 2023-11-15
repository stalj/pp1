import counting
text_count = str(input('Enter text: '))
letter_to_count = str(input('Enter a letter to count: '))
count = counting.count_letters(text_count, letter_to_count)
print(f"The number of letter '{letter_to_count}': {count}")