        
a =  [ [1,'a',['cat'],2] ,[ [[3]],'dog' ],4,5]
newArray = []
def unPack(a):
    for i in a:
        print("i:",i)
        if type(i) != list:
            newArray.append(i)
            print("new: ", newArray)
        else:
            unPack(i)
            
    return newArray
    


def reverseList(a):
    def reverseAgain(b):
        anArray = []
        for i in range(len(b)-1,-1,-1):
            anArray.append(b[i])
        return anArray
        
    emptyArray = []
    
    for i in range(len(a)-1,-1,-1):
        if type(a[i]) != list:
            emptyArray.append(a[i])
        else:
           emptyArray.append(reverseAgain(a[i]))
           
        
    return emptyArray
    
    
        
            
b = [[1, 2], [3, 4], [5, 6, 7]]
print(reverseList(b))

        


