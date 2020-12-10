" " " Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 1253
Output : No
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723 " " "



x=input()

#cant itirate a int so use list comprhension to split in str
num=[int(i) for i in x]  
l=len(num)
final=map(lambda x: pow(x,l), num)

if sum(final)==int(x):
    print(f"num is armstrong ")
else:
    print("num is not armstrong")
