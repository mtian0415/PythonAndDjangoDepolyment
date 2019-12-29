def sayHello(name = 'Sam'):
    print('Hello')
    """
    Prints Hello and then name
    """
    print('Hello ' +name)

sayHello()

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1,3)
print(numSum)

def addOneToNum(num):
    num += 1
    return num
num = 5
new_num = addOneToNum(num)
print(new_num)

getSum = lambda num1, num2: num1 + num2
print(getSum(9,2))

addOneToNum = lambda num: num + 1
print(addOneToNum(5))