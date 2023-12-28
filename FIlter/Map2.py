def main(a):
        if type(a) in [int,float,complex,bool]:
            return a
        else:
            return len(a)
out=map(main,[1,(4,5),[7,9],{1:2}])
print(list(out))
