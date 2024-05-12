def to_upper():
    """Преобразует строку в верхний регистр."""
    text = input().upper()
    print(text)


to_upper()

def capitalize_words(input_str: str) -> str:
    """Функция делает заглавными первые буквы каждого слова в строке. code"""
    return ' '.join(word.capitalize() for word in input_str.split())
