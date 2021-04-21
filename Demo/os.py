

import tarfile
import os

f = []
for (dirpath, dirnames, filenames) in os.walk('d:\\firewall_logs'):
    f.extend(filenames)
print(f)
os.chdir("D:\Firewall_logs")
t = tarfile.open("d:\compose.tar", 'w')
for each in f:
    t.add(each)

t.close()
