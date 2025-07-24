class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [char for char in s if char in 'aeiouAEIOU']
        result = []
        for char in s:
            if char in 'aeiouAEIOU':
                result.append(vowels.pop())
            else:
                result.append(char)
        return ''.join(result)

"""Сложность O(n)"""

    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left, right = 0, len(s) - 1
        vowels = 'aeiouAEIOU'
        while left < right:
            if s_list[left] not in vowels:
                left += 1
            elif s_list[right] not in vowels:
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return ''.join(s_list)

"""Тоже O(n)"""
