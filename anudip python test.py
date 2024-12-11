def remove_non_alpha(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    return result

string = "Hello, World! 123"
print(remove_non_alpha(string))