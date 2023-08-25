class Solution(object):
    string = ''
    length = 0
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.string = s
        for x in range(0, len(s)):
            buffer = []
            buffer.append(s[x])
            index = x
            length = self.checkLongestSubString(buffer, index+1)
            if length > self.length: self.length = length
        return self.length
    def checkLongestSubString(self, buffer, index):
        character = self.string[index] if len(self.string) > index else ''
        if character and character not in buffer:
            buffer.append(character)
            length = self.checkLongestSubString(buffer, index+1)
        return len(buffer)