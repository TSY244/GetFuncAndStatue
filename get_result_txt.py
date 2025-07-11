
fileName="input.txt"


lines=[]
with open(fileName,'r') as f:
    lines=f.readlines()


for line in lines:
    if line.startswith("函数:"):
        splited=line.split()
        if len(splited)==3:
            print(splited[1]+"-"+splited[2])