# 49. Group Anagrams
# Medium
# Topics
# Companies

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"] 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

 

# Constraints:

#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lowercase English letters.

# strs = ["eat","tea","tan","ate","nat","bat"]
# {
#     1:["eat","tea","tan","ate","nat","bat"]
# }
# "eat" => reg = \b[eat]+\b
# wordList = ["eat","tea","tan","ate","nat","bat"]
# subList = []
# is "eat" matched the reg? yes => subList = ["eat"]
# is "tea" matched the reg? yes => subList = ["eat","tea"]
# is "tan" matched the reg? no => subList = ["eat","tea"]
# is "ate" matched the reg? yes => subList = ["eat","tea","ate"]
# is "nat" matched the reg? no => subList = ["eat","tea","ate"]
# is "bat" matched the reg? no => subList = ["eat","tea","ate"]

# result = [["eat","tea","ate"]]

# "tea" 
# is "tea" in the result? yes => skip

# "tan"
# is "tan" in the result? no => make reg = \b[tan]+\b

# import re

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = list()
        for word in strs:
            print(f"word {word}")
            print(f"self.isInList(result, word): {self.isInList(result, word)}")
            print(f"result {result}")
            if self.isInList(result, word) == False:
                # strReg = self.getReg(st)
                # matchingWords = [word for word in strs if re.fullmatch(strReg, word)]
            
                matchingWords = [st for st in strs if self.isMatchedCharacters(st, list(word)) ]
               
                print(f"matching_words: {matchingWords}")
                result.append(matchingWords)
        return result

    def isMatchedCharacters(self, word: str, chars: list[str]) -> bool:
        if len(chars) == 0 and len(word) == 0:
            return True
        elif len(chars) > 0 and len(word) > 0:
            tempStrCount = 0
            isMatched = True
            for c in chars:
                # print(f"st {st}")
                # print(f"c {c}")
                isMatched = isMatched and c in word
                if isMatched == True:
                    tempStrCount += 1
                else:
                    tempStrCount -= 1
            return isMatched and tempStrCount == len(word) and sorted(list(word)) == sorted(chars)
        return False
    
    # def getReg(self,str: str):
    #     return rf'\\b[{str}]+\\b'

    def isInList(self, strs: list[list[str]], str: str) -> bool:
        for strList in strs:
            if str in strList:
                return True
        return False



solution = Solution()
#test if a word is in double lists:
# test_list = [["eat","tea","ate"]]
# test_true1 = solution.isInList(test_list,"eat")
# test_false1 = solution.isInList(test_list,"tan")
# test_false2 = solution.isInList(test_list,"eee")
# print(f"Should be True: {test_true1}")
# print(f"Should be False: {test_false1}")
# print(f"Should be False: {test_false2}")

# result1 = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# print(f"result1: {result1}")

# result2 = solution.groupAnagrams(["","b"])
# print(f"result2: {result2}")

result2 = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat","eee","atee"])
print(f"result2: {result2}")