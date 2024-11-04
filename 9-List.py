# 9. List Comprehension
# Exercise: Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.
number = [i**2 for i in range(0, 11) 
          if i%2==0]
print(number)
