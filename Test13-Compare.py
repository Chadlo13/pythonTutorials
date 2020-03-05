
def maxFunc (num1,num2,num3):
    return max(num1,num2,num3)

input1 = input("Enter a number: ")
input2 = input("Enter a number: ")
input3 = input("Enter a number: ")


maxNum = maxFunc(int(input1),int(input2),int(input3))
print("the largest value is: " + str(maxNum))