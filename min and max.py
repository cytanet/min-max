a = [14, 2, 410, 780, 47, 46, 8, 963, 10]
b = 0
min = a[b]
max = a[b]
while b < len(a):
    if a[b] < min:
        min = b
        min = a[b]
    if a[b] > max:
        max = b
        max = a[b]
    b = b + 1
print(min, max)
