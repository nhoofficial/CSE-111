#medium3
ans={}
Dict={}
s=input().split(',')
for i in s:
    x=i.split(':')
    Dict[x[0]]=x[1]
for a,b in Dict.items():
  if b in ans:
    ans[b].append(a)
  else:
    ans[b] = [a]
print(ans)


