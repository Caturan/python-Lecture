"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

# Method 1: 
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']  
        vowels = set('aeiouAEIOU')

        vowel_indices = [i for i, char in enumerate(s) if char in vowels]
        vowel_chars = [s[i] for i in vowel_indices]

        vowel_chars.reverse()

        s_list = list(s)

        for index, char in zip(vowel_indices, vowel_chars):
            s_list[index] = char 

        return ''.join(s_list)
    
# What is the zip?
# The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable, where corresponding elements from the input iterable are paired together as tuples


# Method 2:
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        vowel = "aeiouAEIOU"
        st = list(s)
        while i < j:
            if st[i] in vowel and st[j] in vowel:
                temp = st[i]
                st[i] = st[j]
                st[j] = temp
                i+=1
                j-=1
            if st[i] not in vowel:
                i+=1
            if st[j] not in vowel:
                j-=1
        
        return "".join(st)