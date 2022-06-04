# Q1.
def rev(x):
    y = x[::-1]
    print("The Reversed String is : ", y)


string = input("Enter the String : ")
rev(string)


# Q2.
def min_max(a, b, c, d):
    print("The Maximum value : ", max(a, b, c, d))
    print("The Minimum value : ", min(a, b, c, d))


p, q, r, s = input("Enter four values to find minimum and maximum value (separated by space) : ").split()
# Split function assigns separate values to separate variables simultaneously
min_max(p, q, r, s)


# Q3.
def sum_4(a, b, c, d):
    sum = a + b + c + d
    print("The Sum of the input is: ", sum)


p = float(input("Enter the first value: "))
q = float(input("Enter the second value: "))
r = float(input("Enter the third value: "))
s = float(input("Enter the fourth value: "))
sum_4 (p, q, r, s)


# Q4.
print("The Number of Local Variables in the given User Defined Function is: ", sum_4.__code__.co_nlocals)
# User_Defined_Function_Name.__code__.co_nlocals


# Q5.
list = list(map(float, input("Enter a list of 8 numbers separated by space: ").split()))
L = len(list)

if (L == 8):
    print("The Even Numbers are : ")
    for num in list:
        if (num % 2 == 0):
            print(num, end=" ")
else:
    print("There are less than 8 elements in the list")