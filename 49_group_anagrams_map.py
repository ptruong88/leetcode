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
        wordMap = dict()
        for word in strs:
            sortedWord = self.sortWord(word)
            # print(f"sortedWord: {sortedWord}")
            wordList = wordMap.get(sortedWord)
            # print(f"wordList: {wordList}")
            if wordList is None:
                wordList = [word]
                wordMap[sortedWord] = wordList
            else:
                wordList.append(word)
        # print(f"wordMap: {wordMap}")
        # print(f"values {wordMap.values()}")
        return list(wordMap.values())

    def sortWord(self, word: str) -> str:
        chars = list(word)
        chars.sort()
        return "".join(chars)


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