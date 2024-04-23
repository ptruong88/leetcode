// https://leetcode.com/problems/valid-parentheses/

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//     Every close bracket has a corresponding open bracket of the same type.

 

// Example 1:

// Input: s = "()"
// Output: true

// Example 2:

// Input: s = "()[]{}"
// Output: true

// Example 3:

// Input: s = "(]"
// Output: false

 

// Constraints:

//     1 <= s.length <= 104
//     s consists of parentheses only '()[]{}'.

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var openBrackets = [];
    for(var i = 0; i < s.length; i++){
      var char = s.charAt(i);
      if( isOpenBracket(s.charAt(i)) ){
        openBrackets.push(char);
      } else {
        var openBracket = openBrackets.pop();
        if( !isValidParenthese(openBracket, char) ){
          return false;
        }
      }
    }
    return openBrackets.length == 0;
};

var isOpenBracket = function(openBracket){
  return CLOSE_BRACKET[openBracket] !== undefined;
};

var isValidParenthese = function(openBracket, closeBracket){
  return CLOSE_BRACKET[openBracket] == closeBracket;
};

var CLOSE_BRACKET = {
 '(': ')',
 '[': ']',
 '{': '}'
};

// ()[]{}
// is open, go next
// is not open, is the previous

// (([[{{

// ([{}])  
// ([{{[(