# Q1
print("To convert a given temperature from deg C to deg F")
a = 40  # degree celsius
b = a*1.8 + 32
print(a, " degree celsius converted to  ", b, "Fahrenheit")


# Q2

print("To check if number m is divisible by number n")
m = int(input("Number m : "))
n = int(input("Number n : "))
if m % n == 0 :
    print(m, "is divisible by ", n)
else:
    print(m, "is not divisible by ", n)


# Q3
print("To check whether given integer is odd or even")
c = int(input("Enter an integer : "))
if c % 2 == 0 :
    print(c, "is even")
else:
    print(c, "is odd")


# Q4
print("To create a user defined function to obtain sum of first n natural number ")
num1 = int(input("Enter number up to which we want sum "))
i = 1
sum1 = 0
while i <= num1:
     sum1 = sum1 + i
     i = i + 1
print("Sum of first n numbers is", sum1)

print("To create a user defined function to obtain sum of square of first n natural number")
num2 = int(input("Enter number up to which we want sum "))
j = 1
sum2 = 0
while j <= num2:
    sum2 = sum2 + (j*j)
    j = j+1
print("sum of square of first n natural number is", sum2)


# Q5
print("To obtain sum of first n odd numbers")
limit = int(input("Enter limit "))
k = 1
sum3 = 0
while k <= limit:
     sum3 = sum3 + k
     k = k+2
print("Sum of n odd no. is", sum3)


# Q6
print("To obtain sum of first n even numbers")

n = int(input("How many even no.s you want to add  "))
l = 1
sum4 = 0
count = 1
while count <= n:
    if (l%2 == 0):
        sum4 = sum4 + l
        count = count + 1
    l = l+1
print("Sum of even no.s=", sum4)


# Q7
print("To find and print the A-B and B-A of two sets A and B")
def A_B(A, B):
    A_minus_B = A - B
    B_minus_A = B - A
    print("Set A minus Set B (A-B) is :", A_minus_B)
    print("Set B minus Set A (B-A) is :", B_minus_A)


A = {"a", "b", "c", "d"}  # Given
B = {"b", "c", "e"}  # Given
A_B(A, B)


# Q8
print("To calculate and print sum and sum of square of given numbers: 20, 12, 15, 1, 7, 10, 5, 1, 15, 5")
x = [20, 12, 15, 1, 7, 10, 5, 1, 15, 5]
y = 1
sum5, sum6 = 0, 0
while y <= x:
    sum5 = sum5 + y
    sum6 = sum6 + (y*y)
    y = y + 1
print("Sum of given numbers is", sum5)
print("sum of square of first n natural number is", sum6)