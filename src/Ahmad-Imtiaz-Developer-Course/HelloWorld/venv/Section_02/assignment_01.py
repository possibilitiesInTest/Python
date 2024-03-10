# Assignment 1:
"""
Print Bill's salary from the my_list object shown below.

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

"""


# your code below:

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

# salary = my_list[0]['Bill']
salary = my_list[0].get('Bill')
print(salary)




































# Solution
# print(my_list[0].get('Bill'))
