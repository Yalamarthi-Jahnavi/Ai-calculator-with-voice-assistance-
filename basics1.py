"""asciivalue ofa numberr
num=int(input("enter a number:"))
print(chr(num))

sum=0
for i in range(65,123):
    print(chr(i),i)
    sum=sum+i
    print(sum)

num=input("enter a number:")
num1=int(num)
print(type(num1))

num=int(input("enter a number:"))
num1=str(num)
print(type(num))

num=float(input("enter float value: "))
print(int(num))

s=input("enter a string or name: ")
print("welcome,",
s)

num=int(input("enter a num:"))
num1=int(input("enter a num:"))
num=num+num1
num1=num-num1
num=num-num1
print(num)
print(num1)

length=int(input("enter length of the rectangle:"))
breadth=int(input("enter breadth of therectangle:"))
area_of_the_rectangle=length*breadth
print("area of the rectangle is:",area_of_the_rectangle)

num=int(input("enter a number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")

num=int(input("enter a number"))
num1=int(input("enter a number"))
if num>num1:
    print("num is greater than num1")
else:
    print("num1 is greater than num")

num=int(input())
num1=int(input())
reminder=num%num1
print(reminder)

num=int(input())
print(num**2)
print(num**3)
"""
num1=int(input())
num2=int(input())
num3=int(input())
average=(num1+num2+num3)/3
print(average)