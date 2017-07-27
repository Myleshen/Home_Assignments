inp_string = "good morning everyone, welcome, starting the session of python programming now"

for index_of_string in range(0,len(inp_string)):
    print(inp_string[index_of_string],end=" ")

word_string = inp_string.split(" ")
print("\n", word_string)

comma_string = inp_string.split(",")
print("\n",comma_string)