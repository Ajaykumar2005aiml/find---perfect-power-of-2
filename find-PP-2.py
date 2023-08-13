num=int(input())
n=2
s=[]
p=1
for i in range(20):
  p=p*2
  s.append(p)
for i in range(len(s)):
  if s[i]>num:
    print(s[i])
    break
