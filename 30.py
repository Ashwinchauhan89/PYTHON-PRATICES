number=int(input("Enter the number"))
temp=number
digit=0
reversed=0
while number>0:
    digit = number%10
    reversed = reversed * 10+ digit
    number = number //10

if temp==reversed:
    print("palidrome")

else:
    print("Not palidrome")


