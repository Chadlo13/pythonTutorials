def mult (num1,num2):
    return num1 * num2

user1 = input("Enter a number: ")
user2 = input("Enter a number: ")

multResult = mult(int(user1), int(user2))

if multResult < int(100):
    print("The result : " + str(multResult) + " is less than 100")
else:
    print("The result : " + str(multResult) + " is greater than 100")


