def is_palindrome(string):
    string="".join(char for char in string if char.isalpha()).lower()
    
    if len(string)<=1:
        return True
    
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

print(is_palindrome("Was it a car or a cat I saw?"))