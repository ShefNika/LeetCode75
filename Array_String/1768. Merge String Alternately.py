class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        length = max(len(word1), len(word2))
        for i in range(length):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return resultth
        
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#        result = []
#        length = min(len(word1), len(word2))
#        for i in range(length):
#            result.append(word1[i])
#            result.append(word2[i])
#        result.append(word1[length:])
#        result.append(word2[length:])
#        return ''.join(result) 

        """Сложность O(m+n)"""
