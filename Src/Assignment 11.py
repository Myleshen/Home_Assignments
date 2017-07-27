inp_string_2 = "a very long string to print. Too big for a normal indexing to work on"

print(inp_string_2[::2])
index = 0
increment = 0
while index < len(inp_string_2):
    print(inp_string_2[index],end="")
    increment = increment + 1
    index = increment + index