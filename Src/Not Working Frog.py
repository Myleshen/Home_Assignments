number_of_elements = [4,-1,1,-3,-6,19]
ans = 0
no_of_jump = 0
for elements in number_of_elements:
    ans = ans + elements
    i = 0
    if ans > number_of_elements[i]:
        no_of_jump = no_of_jump + 1
        print("Came Out")
    else:
        continue
    i = i + 1
