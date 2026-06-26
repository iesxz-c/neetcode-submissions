class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a= {}
        for i in strs:
            k= tuple(sorted(i))
            if k not in a:
                a[k] = [i]
            else:
                a[k].append(i)
        return list(a.values())