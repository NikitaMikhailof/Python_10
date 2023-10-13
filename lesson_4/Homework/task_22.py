var1 = '5 4' 
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

set1 = set([int(i) for i in var2.split()])
set2 = set([int(i) for i in var3.split()])
set3 = sorted(set1 & set2)

print(*set3)

