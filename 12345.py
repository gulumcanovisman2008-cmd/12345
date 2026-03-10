with open('alma.txt','w') as f:
    f.write(input()+'\n')
    f.write(input()+'\n')
    f.write(input()+'\n')
d=0    
with open('alma.txt','r') as f:
    for i in f.readlines():
        d=d+1
print(d)        
        
