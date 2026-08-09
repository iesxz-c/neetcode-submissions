class Solution:
    def isHappy(self, n: int) -> bool:
        def s(n):
            su=0
            while n!=0:
                di = n%10
                su+=di**2
                n=n//10
            return su
        k=set()
        if s(n) ==1 :
            return True
        else:
            n = s(n)
            if n not in k:
                k.add(n)
            
        return False