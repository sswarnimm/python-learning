#Find double spaces in a string.
st = "this is a string with double  spaces"
doublespaces = st.find("  ")
print(doublespaces)

#replace the double space with single space.
st = st.replace("  "," ")
print(st)