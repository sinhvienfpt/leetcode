#Using Math: https://leetcode.com/problems/permutation-sequence/solutions/4960755/python3-clean-code-beat-90-time-and-space-math
from math import factorial

def get_sequence(n,k):
    res = []
    k = k - 1
    for i in range(n-1,0,-1):
        quotient,remainder = k//factorial(i),k%factorial(i)
        res.append(quotient)
        k = remainder
    return res

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        sequence = get_sequence(n,k)
        res = ''
        array = [str(i) for i in range(1,n+1)]
      
        while sequence :
            index = sequence.pop(0)
            res +=array[index]
            del array[index]
        res +=array[0]
      
        return res 
        
