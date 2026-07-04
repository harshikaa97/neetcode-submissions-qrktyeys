class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        for i in range(len(words[0])):
            for word in words:
                if i == len(word) or word[i] != words[0][i]:
                    return word[:i]
        return words[0] 

                
                