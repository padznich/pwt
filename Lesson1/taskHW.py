a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a = []

sum1 = 0
for i in range(0,len(a),2):
    sum1 = sum1 + a[i]

try:
    ans = (sum1 * a[-1])
except:
    ans = 0

print(ans)