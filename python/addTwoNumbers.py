class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        buffer = []
        carry = 0
        print(l1, l2)
        while l1 != None or l2 != None or carry == 1:
            val = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            digit = val + val2 + carry
            summ = (digit if digit < 10 else digit - 10)
            buffer.append(summ)
            carry = 0 if digit < 10 else 1
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        buffer = buffer[::-1]
        print(buffer)
        return self.create_ListNode(buffer)
    def create_ListNode(self, array):
        if len(array) == 1:
            return ListNode(val = array.pop())
        return ListNode(val = array.pop(), next = self.create_ListNode(array))