"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        Yanyana 2 tane tohum olmuyor. 
        boş alan 2n + 1 ve daha fazlası olursa dikilebilir 
        
        0 olanları bulup
        o sayıdan n ile 2n+1 bağlantısı döndürme
   
        
        result = []
        for flower in flowerbed:
            if flower == 0:
                result.append(0)
            else: 
                pass
        diff = len(flowerbed) - len(result) 
        if len(result) >= (2*n)+1:
            if diff >= (2*n)-1:
                return True
            else: 
                return False 
        
"""   


"""
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise. 

    Example 1:

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true

    Example 2:

    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

    Constraints:

        1 <= flowerbed.length <= 2 * 104
        flowerbed[i] is 0 or 1.
        There are no two adjacent flowers in flowerbed.
        0 <= n <= flowerbed.length
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
                empty_next = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_prev and empty_next:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True 
        return count >= n