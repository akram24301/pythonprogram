''' input:"ABCDEFGIJKABC
    output:['ABCDEFG','IJK','ABC']
'''

s='ABCDEFGIJKABC'
out=[]
for i in s:
    if 65<=ord(i)<=91:
        out=out+[i]
print(out)