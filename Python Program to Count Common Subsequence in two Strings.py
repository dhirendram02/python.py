n="ABC"
m="AB"
l1,l2=len(n),len(m)
cnt=[[0 for i in range(l2+1)] for i in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
         if(n[i-1] == m[j-1]):
             cnt[i][j] = 1 + cnt[i][j-1] + cnt[i-1][j]
         else:
             cnt[i][j] = cnt[i][j-1] + cnt[i-1][j] - cnt[i-1][j-1]
print(cnt[l1][l2])
