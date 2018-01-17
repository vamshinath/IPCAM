import os
path=input("Enter path:")
dt=input("Enter date(YYMMDD):")
os.chdir(path)
files=sorted(os.listdir('.'))
mylist=[]
for file in files:
	tmp=(file[7:11])
	mylist.append(tmp)
mylist=set(mylist)
flist=set(map(lambda x:x+"*.264,",mylist))
uhead='wget --user=admin  --password=vamshi81 -r -A "'
utail='" -np -nc "http://192.168.0.108/sd/20'+dt+'/"'

url=uhead
tmp=list(map(lambda x:'A'+str(dt)+'_'+x,flist))
flist=sorted(tmp)

for rg in flist:
	url+=rg

url+=utail

print(url)

