import re
l=0
file = open('test1.txt','r')
count = 0
for line in file:
    count+=1
file2 = open('test2.txt','r')
count2 = 0
for line in file2:
    count2+=1
file3 = open('input.txt','r')
count3 = 0
for line in file3:
    count3+=1
while l < count3 :
    o = open ('input.txt','r')
    l1=3
    l2=0
    y = o.readlines()[l][:-5]
    o1 = open ('test1.txt','r')
    z = o1.readlines()[l1]
    result = re.search (y,z)
    while None == result:
        l1=l1+10
        if l1 > (count):
            break
        o1 = open('test1.txt', 'r')
        z1 = o1.readlines()[l1]
        print (z1)
        result = re.search (y,z1)
        print (result)
        if result != None:
            break
    if None == result:
        e = open ("output.txt",'a')
        e.write('0.0 ')
        l+=1
        continue
    l1=l1+4
    o1 = open('test1.txt', 'r')
    c = o1.readlines()[l1][-3:]
    o2 = open('test2.txt', 'r')
    z2 = o2.readlines()[l2]
    result2 = re.search (c,z2)
    while None == result2:
        l2=l2+2
        if l2 > (count2):
            break
        o2 = open('test2.txt', 'r')
        z2 = o2.readlines()[l2]
        result2 = re.search (c,z2)
        if result2 != None:
            break
    if None == result2:
        e1 = open ("output.txt",'a')
        e1.write('0.0 ')
        l+=1
        continue
    o2 = open('test2.txt','r')
    z2 = o2.readlines()[l2+1][-7:]
    e3 = open('output.txt','a')
    e3.write(z2 )
    l+=1