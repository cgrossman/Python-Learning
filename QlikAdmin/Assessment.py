N=24
t = 0
for k in range(1,N):
    if N % k == 0:
        t += 1
    else:
        t -= 1
print(t)