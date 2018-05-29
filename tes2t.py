
w= int()
w= int(input())


r=1000-w
n5 = int(r / 500)
r=r-n5*500

n1 =int (r/100)
r=r - n1*100

n50=int(r/50)
r=r-n50*50



n10=int(r/10)
r= r- n10*10

r5=int(r/5)
r=r-r5*5

print(str("500 ") +str(n5) +str(" 100:")+ str(n1)+str(n50)+str(n10)+str(r5)+ str(r))