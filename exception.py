# way 1
n = int(input())
for i in range(n):
    ab=input()
    ablist = ab.split()
    a = ablist[0]
    b = ablist[1]
    try:
        A = int(a)
        B = int(b)
        print(A//B)
    except ValueError as e:
        print('Error Code:',e)
    except ZeroDivisionError as e:
        print('Error Code:',e)
        
# # way 2        
# n=int(input())
# for _ in range(n):
#     a,b=input().split()
#     try:
#         print(int(a)//int(b))
#     except ZeroDivisionError as e:
#         print("Error Code: ",e)
#     except ValueError as e:
#         print("Error Code: ",e)
        
# # way 3    
# for i in range(int(input())):
#     a,b = input().split()
#     try:
#         print(int(a)//int(b))
#     except Exception as e:
#         print("Error Code:",e)