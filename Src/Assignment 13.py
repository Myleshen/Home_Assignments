inp_string = "one two one three one four one five one six"
list_1 = inp_string.split("one")
print(list_1[3])


index = int(0)
save_string = inp_string
count = inp_string.count("one")
while count > 0:
    sub_string = inp_string[inp_string.find("one") + len("one"):]
    test_sub_string = inp_string[:inp_string.find("one") + len("one")]
    #index = inp_string.find("one")  + index
    index = abs (len(sub_string) - len(save_string)) - len("one")
    inp_string = sub_string
    count = count - 1
    print(index)
    #print(test_sub_string)
    #print(sub_string)


#Code Below Is Running Properly
"""
index = int(0)
for loop_index in range(0, len(inp_string)):
    if inp_string[index] == 'o' and inp_string[index + 1] == 'n' and inp_string[index + 2] == 'e':
        print(index)
        index = index + 1
    else:
        index = index + 1
        continue
"""