def fname(a):
        if type(a) in [int,float,complex,bool]:
            return True
        else:
            return False
out=filter(fname,[2,10.5,'aaa',{'d':210},(6,20)])
print(list(out))