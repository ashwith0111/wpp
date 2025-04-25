def big(s):
    lis = list(s)
    i = len(lis) - 2
    while i >= 0 and lis[i] >= lis[i + 1]:
        i -= 1
    if i == -1:
        return ''.join(lis)
    j = len(lis) - 1
    while lis[j] <= lis[i]:
        j -= 1
    lis[i], lis[j] = lis[j], lis[i]
    lis = lis[:i + 1] + lis[i + 1:][::-1]
    return ''.join(lis)
n = int(input("Enter the number of cases: "))
i=0
lis=[]
while i<n:
    s = input("Enter a string: ")
    st = big(s)
    if st==s:
        lis.append("no answer")
    else:
        lis.append(st)
    i+=1
for j in lis:
    print(j)