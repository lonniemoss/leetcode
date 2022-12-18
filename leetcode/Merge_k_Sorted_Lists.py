from heapq import heappop, heappush
from tkinter.tix import ListNoteBook, ListNode


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #approach
        # 1. use a heap to store the head of each list
        # 2. pop the smallest head from the heap and append it to the result list
        # 3. push the next node of the popped node to the heap
        # 4. repeat 2 and 3 until the heap is empty
        #time complexity
        # 1. O(nlogk) where n is the number of nodes in the list and k is the number of lists
        #space complexity
        # 1. O(k) where k is the number of lists
        if lists == None or len(lists) == 0:
            return None
        
        dummy = ListNoteBook(-1)
        tail = dummy
        heap = []
        
        #Pushing first values to the heap
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        
        while heap:
            # Poping out the value and index
            temp, i = heappop(heap)
            # Creating a new node and adding to tail and updating tail
            tail.next = ListNode(temp)
            tail = tail.next
            
            # Updating the org Linked List with its Next value ( it will remove the value used)
            lists[i] = lists[i].next
            if lists[i]:
                # Pushing the value to the LL
                heappush(heap, (lists[i].val, i))
            
        return dummy.next
        
       