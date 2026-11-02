class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list()
        list2 = list()
        for i in s:
            list1.append(i)
        for i in t:
            list2.append(i)
        list1.sort()
        list2.sort()
        return list1 == list2    