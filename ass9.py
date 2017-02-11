su=0
for i in range(0,5):
    x=int(raw_input("enter marks"))
    su=su+x
per=su/5
if per<35:
    print "FAIL "
else:
    print "PASS"
