class Solution(object):
    string = ''
    substring = ''
    index_reached = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.string = s
        for x in range(0, len(s)):
            buffer = []
            buffer.append(s[x])
            index = x
            if index + 1 < len(self.string) and self.string[x] == self.string[x+1]: self.checkLongerPalindrome(buffer + buffer, index+1)
            self.checkLongerPalindrome(buffer, index)
            # print(buffer, index)
        return ''.join(self.substring)
    def checkLongerPalindrome(self, buffer, index):
        temp_buffer = [self.string[index-len(buffer)]] + buffer + [self.string[index+1]] if index-len(buffer) >= 0 and index < len(self.string)-1 and self.string[index-len(buffer)] == self.string[index+1] else None
        # print(buffer, temp_buffer, index-len(buffer), index)
        if not temp_buffer:
            self.substring = buffer if len(self.substring) < len(buffer) else self.substring
            return
        self.substring = temp_buffer if len(self.substring) < len(temp_buffer) else self.substring
        self.checkLongerPalindrome(temp_buffer, index+1)