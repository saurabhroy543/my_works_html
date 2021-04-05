'''Amazon question 2. find the id's of the 2 list element in which
 one is id and 2nd is the useage of target ,so find all the pairs of
 id's from a and b which uses the maximum of target'''

a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
c=[]
d=[]
e=[]
for i in a:
    for j in b:
        if i[1]+j[1]<=target:
            sum=i[1]+j[1]
            c.append(sum)
            d.append([i[0],j[0]])
m=max(c)
for i in c:
    if i==m:
        e.append(d[count])
    count=count+1
print(e)
