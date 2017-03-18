# replacing space in a string with '%20'

def replaceWith20(str):
    if len(str)>0:

        counter = 0
        for c in str:
            if c == ' ':
                counter += 1

        if counter>0:
            newsize = len(str)+(2*counter)
            arr = [None]*newsize

            j=newsize-1
            i = len(str)-1
            while(i>=0):
                if str[i]==' ':
                    arr[j] = '0'
                    arr[j-1]= '2'
                    arr[j-2]= '%'
                    j=j-3
                else:
                    arr[j]=str[i]
                    j=j-1
                i=i-1
            return "".join(arr)
        else:
            return str

                

print(replaceWith20("H e l l o "))

