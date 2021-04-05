a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
c=[]
count=0
d=[]
e=[]
for i in a:
    for j in b:
        if i[1]+j[1]<=target:
            sum=i[1]+j[1]
            c.append(sum)
            id1=i[0]
            id2=j[0]
            d.append([i[0],j[0]])
m=max(c)
for i in c:

    if i==m:
        e.append(d[count])
    count=count+1
print(e)
