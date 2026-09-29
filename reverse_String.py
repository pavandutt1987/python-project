def reverse_string(str):
    #logic 1
    reverse1 = str[::-1]
    print(reverse1)
    
    #logic 2
    reverse = ""
    for ch in str:
        reverse = ch+reverse
    return reverse
print(reverse_string("python"))