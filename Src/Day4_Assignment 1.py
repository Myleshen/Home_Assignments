def mul_tab(table, mul_inc):
    ans = table * mul_inc
    return (temp_list.append(ans))


main_list = []
temp_list = []

for index in range(1, 31):
    if index > 1:
        main_list.append(temp_list)
        temp_list = []
    for index_1 in range(1, 11):
        mul_tab(index, index_1)
main_list.append(temp_list)
temp_list = []
print(main_list)
