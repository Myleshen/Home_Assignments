def prime(element):
    for index in range (2,element):
        if element % index == 0:
            return 0
    return 1

ans = 2
no_of_element = int(input())
for index in range(3,no_of_element):
    if prime(index):
        ans = ans + index
        if ans <= no_of_element and prime(ans):
            print(ans)
