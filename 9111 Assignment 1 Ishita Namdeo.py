Name = "Ishita Namdeo"
Roll_no = 9111


# Lists

A = ["Ishita", "Namdeo", 21, "Student"]
B = ["SP College", "Autonomous", "Sadashiv Peth", 411030]
print(A)
print(B)


# Tuples

a = ("Ishita", "Namdeo", 21, "Student")
b = ("SP College", "Autonomous", "Sadashiv Peth", 411030)
print(a)
print(b)

print(A[0:2])
print(B[2:3])
print(a[2])
print(b[3])

# Class
print(type(A))
print(type(B))
print(type(a))
print(type(b))

# Copy
print(A)
A1=A.copy()
print(A1)

# Append
print(B)
B.append("Autonomous")
print(B)

# Count
print(A.count("Ishita Namdeo"))
A.append("Ishita Namdeo")
print(A.count("Ishita Namdeo"))

# Delete
try:
 print(A1)
 del A1
 print(A1)
except:
    pass

# Extend
print(A)
print(B)
A.extend(B)
print(A)

# Index
print(B.index("Sadashiv Peth"))
print(A.index("Autonomous"))

# Sort
K = ["x", "e", "k", "f"]
print(K)
K1 = [4,2,1,3]
print(K1)
K.sort()
K1.sort()
print(K)
print(K1)

# Access
print(K[:2])
print(K1[0:])

# Nested list
ABlist=["Ishita Namdeo", "SP College", [21, 411030]]
print(ABlist)
print(ABlist[2])