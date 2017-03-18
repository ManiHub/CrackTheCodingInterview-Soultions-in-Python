# check if a string is rotation of other 
# eg: "leapp" is rotation of other

# check if str1 is substring of str2
def isSubString(str1, str2):
    if len(str1)<=len(str2):
        return str1 in str2
    else:
        return False

def isRotateExist(str1, str2):
    if len(str1)!=len(str2):
        return False

    str2+=str2

    return isSubString(str1,str2)


print(isRotateExist("leapp","apple"))
print(isRotateExist("leappx","apple"))
