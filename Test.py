a = '''p1 has phone 123
p2 has phone 456
p1 has phone 678
p3 has phone 789'''

#o.p = {"p1":["123","678"],"p2":["456"]..}}

di={}
ar=a.split('\n')
for i in  range(len(ar)) :
    t=ar[i].split(' has phone ')
    if t[0] not in di:
        di[t[0]]=[]
    di[t[0]].append(t[1])
    
print(di)
