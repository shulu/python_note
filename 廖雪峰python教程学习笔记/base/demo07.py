def move(n,a,b,c):
    if n==1:
        print (a, '-->' ,c)
    else:
        move(n-1,a,c,b) 
        move(1,a,b,c)
        move(n-1,b,a,c)     

n=int(input('请输入汉诺塔的层数：'))
move(n,'A','B','C')