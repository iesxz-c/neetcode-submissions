class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre =strs[0] 
        for i in range(len(pre)):
            for word in strs:
                if i == len(word) or pre[i] != word[i]:
                    return pre[:i]
        return pre          