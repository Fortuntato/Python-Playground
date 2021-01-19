#Given a string, find the length of the longest substring without repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Logic to find the substring
    longestCounter = 0
    counter = 1 #starting from 1 because the minimum substring with letters starts from 1
    previousLetter = ''
    for letter in  s:
        print('Checking ' + letter)
        if previousLetter != letter:
            counter = counter + 1
        else:
            if counter > longestCounter:
                longestCounter = counter
            counter = 1
        previousLetter = letter
    return str(longestCounter)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))