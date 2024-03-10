# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""
# Your Code Below:


def separate(s):
    # l = []
    # for elm in s:
    #     l += elm
    # return l
    return list(s)


s = "STRING"
print(separate(s))










































# Solution Below:

# def separate(str):
#     return list(str)
#
# print(separate("hello there"))