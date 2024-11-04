# 10. Removing Duplicates
# Exercise: Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

def remove_duplicates(duplist):
    noduplist = []

    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)

    return noduplist

print(remove_duplicates(nums))
