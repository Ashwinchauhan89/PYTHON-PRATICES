number=int(input("Enter"))
digit=0
reverse=0
while number>0:
    digit =number%10
    reverse = reverse * 10 + digit 
    number = number // 10

print("jgdsyf ",reverse)
