class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_altitude = 0
        max_altitude = cur_altitude
        for i in gain:
            cur_altitude += i
            if max_altitude < cur_altitude:
                max_altitude = cur_altitude
        return max_altitude

  """Сложность O(n)"""
