def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("А роза упала на лапу Азора"))
print(is_palindrome("Привет"))
print(is_palindrome("А роза упала на лапу Азора!"))
print(is_palindrome("12321"))
print(is_palindrome(""))