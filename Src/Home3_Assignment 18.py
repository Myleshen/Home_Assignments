base_number = int(input())
power_raise = int(input())
power_value = int(1)
for index_loop in range(0,power_raise):
    power_value = power_value * base_number
print("Power using For Loop is = ",power_value)

print("\nNow In While Loop\n")

power_value = int(1)
while power_raise > 0:
    power_value = power_value * base_number
    power_raise = power_raise - 1
print("Power using While Loop is = ",power_value)
