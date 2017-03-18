# checking if given string is a permutation of a palindrome string

def canFormPalindrome(str):
    if len(str)==0 or len(str)==1:
        return True
    map=dict()

    for c in str:
        if c in map:
            map[c]=int(map.get(c))+1
        else:
            map[c]=1
    prefix=""
    sufix=""
    root=""
    for c in map:
        if map[c]%2==0:
            l=map[c]
            for i in range(0,l//2):
                prefix+=c
                sufix+=c
            
        else:
            if len(root)>0:
                return False
            else:
                for i in range(0,map[c]):
                    root+=c
    return "".join(prefix+root+ "".join(reversed(sufix))),True
            
    

print(canFormPalindrome("abcabcd"))