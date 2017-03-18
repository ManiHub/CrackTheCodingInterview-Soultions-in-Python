# check if given string contain unique characters

#with out buffer
def isUnique(str):
    if len(str)==0 or len(str)==1:
        return True
    else:
        checker = 0
        for c in str:
            val = ord(c) - ord('a')
            if checker & (1<<val):
                return False
            else:
                checker |= (1<<val)
        return True

# with buffer
def isUnique2(str):
    if len(str)==0 or len(str)==1:
        return True
    else:
        map=[]
        for c in str:
            if c not in map:
                map.append(c)
            else:
                return False
        return True
print(isUnique("abc"))
print(isUnique("abcc"))

print(isUnique2("abc"))
print(isUnique2("abcc"))