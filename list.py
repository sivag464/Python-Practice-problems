N = 2
list = []
for i in range(N):
    tmp = input().split()
    if(tmp[0]== 'insert'):
        list.insert(int(tmp[1]), int(tmp[2]))
    elif( tmp[0]== 'print'):
        print(list)
    elif( tmp[0] == 'remove'):
        list.remove(int(tmp[1]))
    elif( tmp[0] == 'append'):
         list.append(int(tmp[1]))
    elif( tmp[0] == 'sort'):
         list.sort()
    elif( tmp[0] == 'pop'):
        list.pop()
    elif( tmp[0] ==  'reverse'):
        list.reverse()
print(list)










