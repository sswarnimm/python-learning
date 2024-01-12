#key-value
#mydict = {key:value}
mydict = {
    "Swarnim":"my name",
    "Shrivastava":"my surname",
    "marks": [1,2,3],
    "girl" : {"awesome":"she"}#nested dictionary

}

#if we want to extract and print the value of any key

print(mydict["Swarnim"])
print(mydict["Shrivastava"])
mydict["marks"]= [55,84]
print(mydict["marks"])
print(mydict["girl"]["awesome"]) #nested dictionary

#properties of python dictionary-
#1. It is unordered.
#2. It is mutable.
#3. It is indexed.
#4. Cannot contain duplicate keys.