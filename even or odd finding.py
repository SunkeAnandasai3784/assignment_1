givennumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in givennumbers:
        if not i % 2:
            even+=1
        else:
            odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
