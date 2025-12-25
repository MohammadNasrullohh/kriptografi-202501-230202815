import random

p = 208351617316091241234326746312124448251235562226470491514186331217050270460481

secret = 12345   
k = 3            
n = 5           


coefficients = [secret] + [random.randint(1, p - 1) for _ in range(k - 1)]

def polynomial(x):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * (x ** i)
    return result % p


shares = [(x, polynomial(x)) for x in range(1, n + 1)]

print("Shares yang dihasilkan:")
for share in shares:
    print(share)


def lagrange_interpolation(x, points):
    total = 0
    for i in range(len(points)):
        xi, yi = points[i]
        li = 1
        for j in range(len(points)):
            if i != j:
                xj, _ = points[j]
                li *= (x - xj) * pow(xi - xj, -1, p)
                li %= p
        total += yi * li
        total %= p
    return total


recovered_secret = lagrange_interpolation(0, shares[:k])

print("\nRahasia asli      :", secret)
print("Rahasia direkonstruksi:", recovered_secret)
