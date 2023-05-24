class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        # If the length of both strings is not equal, return False
        if len(s) != len(goal):
            return False
        
        # If the strings are equal, check if there are any duplicate characters to swap
        if s == goal:
            return len(set(s)) < len(s)
        
        # Initialize two lists to store the positions of different characters in s and goal
        diff_s, diff_goal = [], []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_s.append(i)
                diff_goal.append(goal[i])
        
        # If the number of different characters is not exactly 2, return False
        if len(diff_s) != 2:
            return False
        
        # Check if the characters at the different positions can be swapped to form the goal string
        return s[diff_s[0]] == diff_goal[1] and s[diff_s[1]] == diff_goal[0]
