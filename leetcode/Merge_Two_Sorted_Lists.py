class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #You are given the heads of two sorted linked lists list1 and list2.
        #Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
        #Return the head of the merged linked list.
        #approach
        #1. create a dummy node
        #2. create a pointer to the dummy node
        #3. while list1 and list2 are not None
        #4. if list1.val is less than list2.val
        #5. set pointer.next to list1
        #6. set list1 to list1.next
        #7. else
        #8. set pointer.next to list2
        #9. set list2 to list2.next
        #10. set pointer to pointer.next
        #11. if list1 is not None
        #12. set pointer.next to list1
        #13. else
        #14. set pointer.next to list2
        #15. return dummy.next
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
        # dummy node
        