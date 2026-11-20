class Solution:
    def label(self,word):
        counts = {}
        chars = sorted(word)
        for letter in chars:
            if letter in counts:
                counts[letter]+=1
            else:
                counts[letter] = 1
        return str(counts)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            word = strs[i]
            key = self.label(word)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
