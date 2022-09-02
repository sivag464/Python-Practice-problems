 
# finda string - hackerank

def count_substring(string, sub_string):
    count = 0
    x = len(string)
    y = len(sub_string)
    for i in range(x):
        if string[i:i+y] == sub_string:
            count+=1
    return count
    
# another method  - startswith

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count

print(count_substring('absdssfab','ab'))