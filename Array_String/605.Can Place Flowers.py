class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if n > len(flowerbed) - sum(flowerbed):
            return False
        flowerbed_ = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed_)-1):
            if flowerbed_[i-1] == flowerbed_[i] == flowerbed_[i+1] == 0 and n > 0:
                flowerbed_[i] = 1
                n -= 1
        return n == 0

  """Сложность O(n)"""
