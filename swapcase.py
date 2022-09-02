
def swap_case(s):
    new_str = ""
    for i in range(len(s)):
        if s[i].isupper():
            new_str = new_str + s[i].lower()
        elif s[i].islower:
            new_str = new_str + s[i].upper()
        else:
            new_str = new_str + i     
    return new_str
output = swap_case('Hi Hello Im SIVA')
print(output)
