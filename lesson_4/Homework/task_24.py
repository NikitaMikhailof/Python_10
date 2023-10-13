arr = [5, 8, 6, 4, 9, 2, 7, 3] 

res = []

for i in range(1, len(arr) - 1):
    berryLeft = arr[i - 1]
    berryRight = arr[i + 1] 
    summa = berryLeft + berryRight + arr[i] 
    res.append(summa)
print(max(res))    