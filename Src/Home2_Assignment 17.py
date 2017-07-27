inp_num = int(input())
num_sum = int(0)
for index in range(0, inp_num + 1):
    num_sum = num_sum + index
print("Sum Using For Loop is =  ",num_sum)

num_sum = int(0)
while inp_num > 0:
    num_sum = num_sum + inp_num
    inp_num = inp_num - 1
print("Sum Using While Loop is = ",num_sum)

