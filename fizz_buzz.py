def num():
    n = 1
    while n <= 100:
     print(n)
     n = n+1

# If the number is a multiple of 3, print "Fizz" instead of the number.
def multiple(num):
    if num % 3 == 0:
     print("Fizz")

# If the number is a multiple of 5, print "Buzz" instead of the number.
def multi(num):
    if num % 5 == 0:
     print("Buzz")

# If the number is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
def multi1(num):
    if num % 5 == 0 and num % 3 == 0:
     print("FizzBuzz")
num()
multiple(6)
multi(25)
multi1(15)