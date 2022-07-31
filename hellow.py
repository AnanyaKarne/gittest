f=open('numbers.txt','w')

with f:
    for i in range(0,10000):
        f.write(str(i)+"\n")

