st = input("Give the string: ")
st = st.lower()
s = set(st)
if len(s)>=27:
    print("panagram")
else:
    print("not panagram")