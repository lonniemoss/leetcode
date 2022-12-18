class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #approach
        #1. use two pointers, one fast and one slow
        #2. if there is a cycle, the fast pointer will catch up with the slow pointer
        #3. if there is no cycle, the fast pointer will reach the end of the list
        #4. return false if fast pointer is None
        #5. return true if fast pointer is equal to slow pointer
        #6. return false if fast pointer is not equal to slow pointer

        #time complexity
        #1. O(n) where n is the number of nodes in the list
        #space comlexity
        #1. O(1) constant space

        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # fast and slow pointer
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        #Given head, the head of a linked list, determine if the linked list has a cycle in it.
        #There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
        #Return true if there is a cycle in the linked list. Otherwise, return false.