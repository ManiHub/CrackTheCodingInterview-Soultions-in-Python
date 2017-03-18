# checking if given two strings are one replacement/one insert/one delete away from each other

def check(str1, str2):
    if len(str1)==len(str2):
        return onerepalce(str1,str2)
    elif len(str1)+1==len(str2):
        return oneInsert(str1, str2)
    elif len(str1)-1==len(str2):
        return oneInsert(str2,str1)
    else:
        return False

def onerepalce(str1,str2):
    if len(str1)!=len(str2):
        return False
    found=False

    for s1,s2 in zip(str1,str2):
        if s1 != s2:
            if found:
                return False
            else:
                found=True
    return True


# insertion and deletion is one and the same
def oneInsert(str1,str2):
    index1=0
    index2=0
    while(index1<len(str1) and index2<len(str2)):
        if str1[index1]!=str2[index2]:
            if index1!=index2:
                return False
            index2+=1
        else:
            index1+=1
            index2+=1
    
    return True

print(check("apple","aple"))
print(check("apple","appli"))
print(check("apple","appliX"))
print(check("apple","apple3"))
