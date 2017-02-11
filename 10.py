def simple_interest(p,t,i):
    a=p*t*i*0.01
    return a
p=input("please enter the principal amount")
t=input("please enter the time per year ")
i=input("please enter the interest of loan percentage")
print simple_interest(p,t,i)
