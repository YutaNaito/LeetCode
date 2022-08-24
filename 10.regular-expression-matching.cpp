/*
 * @lc app=leetcode id=10 lang=cpp
 *
 * [10] Regular Expression Matching
 */

// @lc code=start

#include <regex>
#include <string>

using namespace std;

class Solution {
public:
  bool isMatch(string s, string p) {
    std::regex reg(p);
    return std::regex_match(s, reg);
  }
};
// @lc code=end
