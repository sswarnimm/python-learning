#key-value
#mydict = {key:value}
mydict = {
    "Swarnim": "my name",
    "Shrivastava":"my surname",
    "marks": [1, 2, 3],
    "girl" : {"awesome": "she"},#nested dictionary
    1:2

}

print(mydict.keys()) #by defalt type is dict_keys
print (list(mydict.keys())) #through type casting we can change to list type
print (list(mydict.values())) #through type casting we can change to list type
print (list(mydict.items())) #give key value pair of whole dictionary

print(mydict)
updatedict = {"home": "pune",
              "sahil": "husband",
              "girl": "harshita"} #will update the original one if repeated

mydict.update(updatedict)  #Updates the dictionary by adding key-value pairs from updatedict
print(mydict)

#.get method of dictionary - the output will be same with or without get

print(mydict.get("Swarnim")) #print value associated with "Swarnim"
print(mydict["Swarnim"])

#but if we try to print a key value which is not present in the dictioary, then get will return none wheres other will throw error.

#difference between get() and [""]

print(mydict.get("Swarnim2")) #returning none
print(mydict["Swarnim2"]) #returning error









