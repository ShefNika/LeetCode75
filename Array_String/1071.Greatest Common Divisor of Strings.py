    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ''
        if str1 + str2 != str2 + str1:
            return result
        length = min(len(str1), len(str2))
        for i in range(length):
            if str1[i] == str2[i]:
                result += str1[i]
        for i in range(1,len(result)+1):
            if result[:i]*(len(result)//i) == result:
                result = result[:i]
                break
        return result
      """ О(n^2)"""

    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     if str1 + str2 != str2 + str1:
    #         return ""
    #     gcd_length = math.gcd(len(str1), len(str2))
    #     return str1[:gcd_length] 

"""O(m+n)"""
