

a = dict()
a["user"] = 5
a["priyank"]  = 10
print(a)
b = sorted(a,key=a.get,reverse=True)
for c in b:
    print(f"{c} {a[c]}")

detail = dict()
for line in open("/etc/fstab"):
    if "/dev/" in line :
        uuid = line.split()[0],split("/")[1]
        out = Popen(r"lsbkl -n -output=uuid", shell=True)
        detail[uuid] = out


pyout = open("d:\pythonoutputfile.txt", "w")
print("Lets do it .... ",file=pyout)
pyout.close()
import os
os.remove("d:\pythonoutputfile.txt")
os._exists("d:\pythonoutputfile.txt")