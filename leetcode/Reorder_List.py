class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #approach
        #1. find the middle of the list
        #2. reverse the second half of the list
        #3. merge the two lists
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
        # find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # merge the two lists
        first = head
        second = prev
        while second.next:
            next = first.next
            first.next = second
            first = next
            next = second.next
            second.next = first
            second = next
        return head
        #Given a singly linked list L: L0→L1→…→Ln-1→Ln,
        #reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
        #You may not modify the values in the list's nodes. Only nodes itself may be changed.