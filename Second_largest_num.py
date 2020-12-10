num=int(input())
l=[]
for i in range(num):
    l.append(int(input()))
l.sort()
l.reverse()
print(l)
for i in range(len(l)):
    if l[i]<l[0]:
        print(f"second highest ele is {l[i]}")
        break
