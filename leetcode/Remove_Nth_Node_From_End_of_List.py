class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #aproach
        #1. find the length of the linked list
        #2. find the node to be removed
        #3. remove the node
        #time complexity
        #1. O(n) where n is the number of nodes in the list
        #space complexity
        #1. O(1) constant space
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # fast pointer
        fast = head
        # slow pointer
        slow = head
        # move fast pointer n steps
        for i in range(n):
            fast = fast.next
        # if fast pointer is None, remove the head node
        if fast is None:
            return head.next
        # move fast and slow pointer until fast pointer is None
        while fast.next:
            fast = fast.next
            slow = slow.next
        # remove the node
        slow.next = slow.next.next
        return head
        #Given the head of a linked list, remove the nth node from the end of the list and return its head.