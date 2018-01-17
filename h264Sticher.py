import os
path=input("Enter path:")
os.chdir(path)
files=sorted(os.listdir('.'))
dst=open("dt:"+files[0].split('_')[0][3:]+"tm:"+files[0].split('_')[-1]+"_"+files[-1].split('_')[-1],"wb")
for x in files:
    tmp=open(x,'rb')
    dst.write(tmp.read())
    tmp.close()
    os.remove(x)
dst.close()
print("videos Combined!")
