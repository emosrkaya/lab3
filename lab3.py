import numpy as np

n = int(input("Matrisin ölçüsünü daxil edin: "))

A = np.random.randint(-10, 11, size=(n, n))

print("Başlanğıc matrisi:")
print(A)

for i in range(n):
    row = A[i]
    positive_elements = row[row > 0]
    if positive_elements.size > 0:
        mean_positive = np.mean(positive_elements)
    else:
        mean_positive = 0  
    A[i, i] = mean_positive

print("\nDəyişdirilmiş matrisi:")
print(A)
