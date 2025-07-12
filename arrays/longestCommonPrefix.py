"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
strs = ["float", "flower", "flow", "flight"]


def longestCommonPrefix(strs):
    output = []
    if len(strs) == 1:
        return strs
    elif len(strs) > 2:
        longestCommonPrefix(strs)
    else:
        for i in range(0, len(strs[0])):
            if strs[0][i] == strs[1][i]:
                output.append(strs[0][i])
            else:
                break
    return [str(output)]


strs = sorted(strs, key=len)
o = longestCommonPrefix(strs)
print(o)
