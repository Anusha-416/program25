str=input("enter a string:")
swapped_string=''
for i in str:
    if ord(i)>=65 and ord(i)<=90:
        swapped_string +=chr(ord(i)+32)
    elif ord(i)>=97 and ord(i)<=122:
        swapped_string+=chr(ord(i)-32)
    else:
        swapped_string +=i
print(swapped_string)
