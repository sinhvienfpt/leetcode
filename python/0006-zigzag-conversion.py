def arrayOfPosistion(s,numRow,i=0,count=0):
    res=[]
    while True:
        while i < numRow:
            res.append(i)
            count += 1
            if count == len(s) :
                return res
            i += 1
        i -= 2
        while i>0:
            res.append(i)
            count +=1
            if count == len(s) :
                return res
            i -= 1
            

class Solution:
    def convert(self,s: str, numRows: int) -> str:
        if len(s) < numRows or numRows==1:
            return s
        
        a = arrayOfPosistion(s,numRows)
        j = 0 
        res = ""
        while j < numRows :
            for i in range(len(a)):
                if a[i] == j :
                    res+=s[i]
            j += 1
        return res
