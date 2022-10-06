A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
BA = dict()

for i in range(len(B)):
    if B[i] not in BA:
        BA[B[i]] = A[i]
    else:
        BA[B[i]] += A[i]

print(BA)