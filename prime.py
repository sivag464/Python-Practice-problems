# 12


lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
list_prime =[]
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    for i in range (2, number):  
        if (number % i) == 0:  
            pass 
    else:  
         list_prime.append(number) 
print(list_prime)