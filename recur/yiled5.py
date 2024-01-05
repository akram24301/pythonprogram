def main(a):
    for i in a:
        if len(i)%2==0:
            yield (i[0]+i[-1])/2
        else:
            yield i[len(i)//2]
out=main([(1,2),[4,5,3],[11,12,13],[9,8,7,6]])
print(list(out))
