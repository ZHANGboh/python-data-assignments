import csv
q=open('trade-wars-news1.txt',encoding='UTF-8')
a=q.read()
w=open('trade-wars-news2.txt',encoding='UTF-8')
s=w.read()
e=open('trade-wars-news3.txt',encoding='UTF-8')
d=e.read()
r=open('trade-wars-news4.txt',encoding='UTF-8')
f=r.read()
y=open('trade-wars-news5.txt',encoding='UTF-8')
g=y.read()
a1=a.split()
s1=s.split()
d1=d.split()
f1=f.split()
g1=g.split()
count_dict={}
for str in a1:
    if str in count_dict.keys():
        count_dict[str]=count_dict[str]+1
    else:
        count_dict[str]=1
count_dict={}
for str in s1:
    if str in count_dict.keys():
        count_dict[str]=count_dict[str]+1
    else:
        count_dict[str]=1
 count_dict={}
for str in d1:
    if str in count_dict.keys():
        count_dict[str]=count_dict[str]+1
    else:
        count_dict[str]=1
for str in f1:
    if str in count_dict.keys():
        count_dict[str]=count_dict[str]+1
    else:
        count_dict[str]=1
for str in g1:
    if str in count_dict.keys():
        count_dict[str]=count_dict[str]+1
    else:
        count_dict[str]=1
count_list=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
print(count_list[0:15])
with open('Trade War.csv','w') as aa:
    writer = csv.writer(aa)
    header = ['keyword','frenquency']
    writer.writerow(header)
    for i in range(0,len(count_list)):
        writer.writerow([count_list[i][0],count_list[i][1]])