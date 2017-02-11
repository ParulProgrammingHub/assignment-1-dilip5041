def intr(p,r,t):
  n=r/t
  d=t*t
  i=(p*((1+n)**(d)))-p
  print n
  print d
  print i
a=float(raw_input("principle="))
b=float(raw_input("rate="))
c=int(raw_input("time(in year)="))
intr(a,b,c)
