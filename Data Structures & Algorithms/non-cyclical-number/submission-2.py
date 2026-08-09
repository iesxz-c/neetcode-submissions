class Solution:
    def isHappy(self, n: int) -> bool:
        def s(n):
            su=0
            while n!=0:
                di = n%10
                su+=di**2
                n=n//10
            return su
        if n==1:
            return True
        k=set()
        k.add(n)
        while n!=1:
            n=s(n)
            if n==1 :
                return True
            else:
                if n not in k:
                    k.add(n)
                else:
                    return False