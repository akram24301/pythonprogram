st="255.255.255.2"
temp=st.split('.')
if len(temp)==4:
    for i in temp:
        if i.isnumeric:
            out='YES'
        else:
            out='NO'
            break
else:
    out='NO'
print(out)
    