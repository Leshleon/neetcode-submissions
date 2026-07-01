class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped_anagrams = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] +=1
            mapped_anagrams[tuple(count)].append(word)
        return list(mapped_anagrams.values())
