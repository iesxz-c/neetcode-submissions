from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = Counter(fruits)
        li = list(k.values())
        li.sort(reverse=True)
        return li[0] if len( li)<=1 else li[0]+li[1]
        