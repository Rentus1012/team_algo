def sequential_Search(a,x):
    alist = []
    n = len(a)
    for i in range(0,n,1):
        if x == a[i]:
            #alist.append(i)
            return alist

    return alist

S=[17,92,18,33,58,7,33,42]

print(sequential_Search(S,33))

