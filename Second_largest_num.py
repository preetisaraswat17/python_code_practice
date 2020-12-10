#create list
num=int(input())
l=[]
for i in range(num):
    l.append(int(input()))

#sort list and reverse as sort is in ascending order by default or sort(reverse=True) for descending
l.sort()
l.reverse()
print(l)

#compare only first few and break
for i in range(len(l)):
    if l[i]<l[0]:
        print(f"second highest ele is {l[i]}")
        break
