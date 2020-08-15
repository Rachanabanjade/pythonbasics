# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Sam'): # def sayHello() : no paramater
    print('Hello' + name)
    print(f'Hello {name}')

sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(9,7))

def add(num):
    num +=1
    return num

num = 5
newnum = add(num)
print(newnum)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2

print(getSum(10, 3))



