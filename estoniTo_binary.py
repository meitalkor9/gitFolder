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
