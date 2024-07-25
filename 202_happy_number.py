# 202. Happy Number
# Easy
# Topics
# Companies

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
#     which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:

# Input: n = 2
# Output: false

 

# Constraints:

#     1 <= n <= 2^31 - 1

class Solution:

    def isHappy(self, n: int) -> bool:
        sumList = set()
        return self.isHappyWithSumList(n, sumList)

    def number(self, number: int) -> int:
        quotient = number
        remain = 0
        sum = 0
        while quotient > 0:
            remain = quotient % 10
            quotient = (int)(quotient / 10)
            sum += remain * remain

        return sum
    
    def isHappyWithSumList(self, number: int, sumList: set) -> bool:
        if number == 1:
            return True

        new_number = self.number(number)

        if new_number in sumList:
            return False
        
        sumList.add(new_number)

        return self.isHappyWithSumList(new_number, sumList)
    
    
    

    
        

test1 = Solution()
print(f"test1: {test1.isHappy(19)}")

print(f"test2: {test1.isHappy(3)}")

print(f"test2: {test1.isHappy(7)}")

print(f"test2: {test1.isHappy(139)}")

139+7+3+19
19,7,3,139
