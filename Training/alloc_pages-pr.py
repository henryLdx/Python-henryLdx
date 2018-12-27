import numpy as np
import matplotlib.pyplot as plt
import re
import string
import sys
import os

def usage():
    print("arg[1] is file name,please")

if os.path.isfile(sys.argv[1]):
    pass
else:
    usage()
    exit(1)

fd=open(sys.argv[1], 'r')
fd_content=fd.read()
fd1=open(sys.argv[1]+'_bk', 'w')

str='\n'.join(re.findall('.*' + "us" + '.*' +  "alloc_pages_current" + '.*', fd_content))

fd1.write(str)
fd.close
fd1.close
fd2=open(sys.argv[1]+'_bk', 'r')

count=0
time=[]
times=[]
for lines in fd2.readlines():
    args=re.split(r'\s+', lines)
    #if args[2].isdigit():
    if args[2] == '+':
        temp = args[3]
    else:
        temp = args[2]
    count = count +1
    time.append(temp)
    times.append(count)

plt.figure()
plt.plot(times, time)
plt.xlabel("Times")
plt.ylabel("us")
plt.title("alloc page time")
plt.savefig("alloc_page.jpg")
plt.show()




