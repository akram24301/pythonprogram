def sample(st):
    temp=''
    for i in range(len(st)):
        if st[i] not in st[i+1:] and st[i] not in temp:
            out=i
            break
        elif i==len(st)-1:
            out=-1
        else:
            temp+=st[i]
    return out
print(sample('todaytoday'))