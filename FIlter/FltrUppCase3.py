def upper(a):
    if 'A'<= a<='Z':
        return True
    else:
        return False
out=filter(upper,'aBc@')
print(list(out))
