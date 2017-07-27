list_1 = []
list_2 = []
ans = 0
for table_num in range(1, 31):
    list_2 = []
    for mul_table in range(1, 11):
        ans = table_num * mul_table
        list_2.append(ans)
    list_1.append(list_2)
    #print(list_2)
print(list_1)
