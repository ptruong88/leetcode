// I change this.
// https://leetcode.com/problems/longest-common-prefix/

// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

 

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"

// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

 

// Constraints:

//     1 <= strs.length <= 200
//     0 <= strs[i].length <= 200
//     strs[i] consists of only lowercase English letters.

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length == 1) return strs[0];

    var result = '';
    var prefix = '';
    const selectedWord = strs[0];
    for(var charIndex = 0; charIndex < selectedWord.length; charIndex++){
        var char = selectedWord.charAt(charIndex);
        prefix += char;
        var prefixFoundInOtherWords = isPrefixFoundInOtherWords(prefix, strs);
        if(prefixFoundInOtherWords){
            result = prefix
        }
        else {
            result = prefix.substr(0, prefix.length - 1);
            break;
        }
    }
    
    return result;
};

var isPrefixFoundInOtherWords = function(prefix, strs){
    for(var i = 0; i < strs.length; i++){
        var foundIndex = strs[i].indexOf(prefix);
        if(foundIndex != 0){
            return false;
        }
    }
    return true;
};


// flower

// 0: f
// iterate
// find f in other words
// common1 += f

// 1: l
// iterate
// find l in other words
// common1 += l

// 2: o
// iterate
// not find o in all words
// store common1 to common2
// clear common1 to empty string
// what if there are mulitiple same strings? choose the lastest one?

// 3: w
// iterate
// find w in other words
// common1 += w

// 4: i
// iterate
// find w in other words
// common1 += i

// if common1.length == common2.length, common2 = common1
// if common1.length > common2.length, common2 = common1

// return common2