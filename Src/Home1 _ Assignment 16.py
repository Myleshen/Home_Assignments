num = int(input())
save_num = num
fact_num = int(1)
while num > 0:
    fact_num = num * fact_num
    num = num - 1
print("Factorial Of ",save_num," = ",fact_num)