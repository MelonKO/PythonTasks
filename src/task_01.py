# Разработайте метод is_palindrome(string), который будет определять, является ли
# параметр string палиндромом (строкой, которая читается одинаково как сначала
# так и с конца), при условии игнорирования пробелов, знаков препинания и регистра.


def is_palindrome(string) -> bool:
    processed = ''.join(char.lower() for char in str(string) if char.isalnum())
    if not len(processed):
        return True
    i = 0
    j = len(processed)-1
    while i < j:
        if processed[i] != processed[j]:
            return False
        i += 1
        j -= 1
    return True
