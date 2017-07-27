instance_of_prime = int(input())
count = int(1)
ans = list()

for index in range(1, 100):
    if index == 1 :
        #print("2")
        count = count + 1
    for index_1 in range(2, index):
        if (index % index_1 != 0) and count <= instance_of_prime:
            ans = index
            #print(ans)
            count = count + 1
            break
        if index % index_1 == 0 and count <= instance_of_prime:
            break
print(ans)