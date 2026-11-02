class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list()
        list2 = list()
        list1+=s
        list2+=t
        list1.sort()
        list2.sort()
        return list1 == list2    