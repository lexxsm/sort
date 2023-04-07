n = int(input())
i = 0
j = 0
chisla = []
res_chisla = []
for i in range(n):
    chisla.append(str(input()))
    i += 1
p = int(input())
for j in range(n):
    res_chisla.append(int(chisla[j])**p)
    j += 1
i = 0
print(res_chisla)
for i in range(n):
    print(res_chisla[i])
    i += 1
