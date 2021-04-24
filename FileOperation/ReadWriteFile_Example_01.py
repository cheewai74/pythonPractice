"""
    Example 1: Write to a file
"""
the_file = open("integers.txt", "w")
integers = [1, 2, 3, 4, 5]
for integer in integers:
    the_file.write(str(integer) + '\n')
the_file.close()

"""
    Example 2: Read a file
"""
the_file = open("integers.txt", "w")
lines = the_file.readlines()
for line in lines:
    print(line)
the_file.close()