// # https://leetcode.com/problems/two-sum/
// # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// # You may assume that each input would have exactly one solution, and you may not use the same element twice.

// # You can return the answer in any order.

 

// # Example 1:

// # Input: nums = [2,7,11,15], target = 9
// # Output: [0,1]
// # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// # Example 2:

// # Input: nums = [3,2,4], target = 6
// # Output: [1,2]

// # Example 3:

// # Input: nums = [3,3], target = 6
// # Output: [0,1]

 

// # Constraints:

// #     2 <= nums.length <= 104
// #     -109 <= nums[i] <= 109
// #     -109 <= target <= 109
// #     Only one valid answer exists.

 
// # Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // The idea is we store each number from number list into a map which uses the number as a key and index as a list (in case, there are multi same numbers). 
    // Then we get the remain from the target to each number and use the map to get index for the remain which is the second num. We only care if the index list is not undefined. If the index list contains 1 number, the number is the second index for the result. If the index list contains 2 numbers, the second number is the second index for the result.
    // For example: [3,2,4], target: 6
    // Map: {3:[0], 2:[1], 4:[2]}
    // Remain: iterate the number list 
    // - index 0: 6 - 3 = 3. index from map = 0, equal to the number list index => ignore
    // - index 1: 6 - 2 = 4. index from map = 2, different => the result is [1, 2]

        var result = [];
        var numMap = new Map();
        for(var i = 0; i < nums.length; i++){
            var num = nums[i];
            var indexList = numMap.get(num);
            if(!indexList) indexList = [];
            indexList.push(i);
            numMap.set(num, indexList);
        }

        for(var i = 0; i < nums.length; i++){
            var remain = target - nums[i];
            var indexListFromNumMap = numMap.get(remain);
            var secondIndexForResult;
            if(indexListFromNumMap){
                if(indexListFromNumMap.length > 1){
                    secondIndexForResult = indexListFromNumMap[1];
                } else {
                    secondIndexForResult = indexListFromNumMap[0];
                }
            }

            if(secondIndexForResult !== undefined && secondIndexForResult != i){
                result = [i, secondIndexForResult];
                break;
            }
        }

        return result;
};