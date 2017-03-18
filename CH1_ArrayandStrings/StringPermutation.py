# check if given strig is permutation of other

# with predefine methods
def isPermute(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2 :
        return True
    else:
        return False

#No predefine methods
def isPermute2(str1,str2):

    if len(str1) != len(str2):
        return False

    map = dict()
    # addding Str1 contents to Dict<>
    for c in str1:
        if c in map:
            map[c]=int(map.get(c)+1)
        else:
            map[c]=1

    # checking if str2 contain same number of characters as in str2
    for c in str2:
        if c in map and map[c]>0:
            map[c] = int(map[c])-1
        else:
            return False
    return True



print(isPermute("abc","abc"))
print(isPermute("abc","acb"))
print(isPermute("abc","axb"))

print(isPermute2("abc","abc"))
print(isPermute2("abc","acb"))
print(isPermute2("abc","axb"))