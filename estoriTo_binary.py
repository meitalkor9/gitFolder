num=int(input("enter num"))
bit=int(input("enter amount of bit"))
left=""
while(len(left)<bit):
    left=str(num%2)+left
    num=num//2
print(left)


left2=""
for n in left:
    if n=='1':
        left2=left2+'0'
    else:
       left2=left2+'1'

left2=list(left2)
i=bit-1
while(i>=0):
    if left2[i]=='0':
        left2[i]='1'
        break
    else:
        left2[i]='0'
        i=i-1

result="" 
for i in left2:
    result=result+i
print (result)


