class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        list1 = list()
        list2 = list()
        for i,j in zip(s,t):
            list1.append(i)
            list2.append(j)
        list1.sort()
        list2.sort()
        return list1 == list2    