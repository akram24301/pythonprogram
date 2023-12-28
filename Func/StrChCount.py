
def countch(a,ch):
    count=0
    for i in a:
        if ch==i:
            count+=1
    return count
c=countch('apple','p')
print(c)
