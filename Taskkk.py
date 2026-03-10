with open('alma.txt','w') as f:
    f.write(input() + " " + input() + '\n')
    f.write(input() + " " + input() + '\n')
    f.write(input() + " " + input() + '\n')

d=0    
c=0

with open('alma.txt','r') as f:
    for i in f.readlines():
        c = c + int(i.split()[1])
        d = d + 1

print(c/d)
