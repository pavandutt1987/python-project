def reverse_string(str):
    reverse = ""
    for ch in str:
        reverse = ch+reverse
    return reverse
print(reverse_string("python"))