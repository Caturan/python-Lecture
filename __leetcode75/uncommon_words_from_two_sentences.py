"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour",
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a1 = (s1.split(' '))
        a2 = (s2.split(' '))

        l1 = []
        l2 = []

        i = 0 
        while i < len(a1):
            if a1[i] in a2: 
                pass
            else: 
                l1.append(a1[i])
            i += 1

        i = 0
        while i < len(a2):
            if a2[i] in a1:
                pass 
            else:
                l2.append(a2[i])
            i += 1

        def remove_duplicates(lst):
            duplicates = set([x for x in lst if lst.count(x) > 1])
            return [x for x in lst if x not in duplicates]

        sp1 = remove_duplicates(l1)
        sp2 = remove_duplicates(l2)

        l3 = sp1 + sp2
        return l3