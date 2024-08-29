"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x):
            visited.add(x)
            for y in graph[x]:
                if y not in visited:
                    dfs(y)
            
        graph = {}
        for i, j in stones:
            if i not in graph:
                graph[i] = []
            if ~j not in graph:
                graph[~j] = []
            graph[i].append(~j)
            graph[~j].append(i)
        
        visited = set()
        num_of_components = 0
        for i, j in stones:
            if i not in visited:
                dfs(i)
                num_of_components += 1
        return len(stones) - num_of_components

      
"""
~j ifadesi, Python'da bitwise NOT (bit düzeyinde tersine çevirme) operatörüdür. Bu operatör, bir sayının ikili (binary) temsilini tersine çevirir. Ancak, bu operatör taşlar üzerinde bir graf yapısında sütunları satırlardan ayırt etmek için kullanıldığında biraz kafa karıştırıcı olabilir.

Bitwise NOT Operatörü (~):
~ operatörü, bir sayının ikili temsilinde her bir biti tersine çevirir. Örneğin:
~0 → -1
~1 → -2
~2 → -3
Bu operatör, negatif olmayan bir tam sayıyı negatif bir tam sayıya dönüştürür.

Kullanımı Bu Problemin Çözümünde:
Bu problemde, taşlar (i, j) koordinatlarıyla temsil edilir. Aynı satırda veya sütunda olan taşları bağlamak için bir graf oluşturuyoruz. Ancak, hem satırları (i) hem de sütunları (j) temsil eden düğümleri ayırt etmemiz gerekiyor. Satır ve sütunları aynı "uzayda" temsil etmek yerine, satırları pozitif, sütunları ise negatif sayılarla temsil edebiliriz.

i → Satır (pozitif değer)
~j → Sütun (negatif değer)
Bu şekilde, sütunlar için negatif değerler kullanarak graf içerisinde aynı değerlerin karışmasını engellemiş oluruz. Örneğin, j = 2 ise, ~j işlemi -3 olur (yani ~2 = -3), böylece sütunlar ve satırlar arasında ayrım yapmış oluruz.

Alternatif Yöntem:
~j kullanmak kafa karıştırıcı olabilir. Bunun yerine, sütunları j + 10001 gibi bir işlemle pozitif bir sayı aralığına taşıyarak da ayırabilirsiniz (bu, sütunları satırlardan ayrı bir aralıkta temsil eder).
"""