"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowels = 0
        current_vowels = 0
    
        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels
    
        # Slide the window across the string
        for i in range(k, len(s)):
            if s[i - k] in vowels:  # Remove the leftmost character of the previous window
                current_vowels -= 1
            if s[i] in vowels:      # Add the new rightmost character of the current window
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
    
        return max_vowels