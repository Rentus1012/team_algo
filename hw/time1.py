import random
import time

def generate_list(a, n):
    a.clear()
    for i in range(0, n):
        a.append(random.randrange(0, 1000))
                 

def bubble_sort(a):

    for p in range(len(a)-1, 0, -1):
        for i in range(p):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        return a
    

def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
        
    return len(r)

def ins_sort1(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)

    return result

def ins_sort2(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >=0 and a[j] > key:
            a[j+1] = a[j]
            j-= 1

        a[j + 1] = key

d = []

generate_list(d, 100)
print(d)

start = time.time()
a= ins_sort1(d)
print("time: ", time.time() - start)
print(a)

generate_list(d, 100)
print(d)

start = time.time()
ins_sort2(d)
print("time: ", time.time() - start)
print(d)

generate_list(d, 100)
print(d)

start = time.time()
a= ins_sort1(d)
print("time: ", time.time() - start)
print(a)

