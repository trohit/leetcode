'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

SC: O(n), where n is pos of elem to be removed from the last
TC: O(L), where L is length of linked-list.

Runtime: 49 ms, faster than 36.58% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.1 MB, less than 66.82% of Python3 online submissions for Remove Nth Node From End of List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # egde case 1: 
        t = head
        ll = []
        while t:
            if len(ll) > n:
                ll.pop(0)
            ll.append(t)
            t = t.next
        print(f"will remove {ll[n*-1].val}")
        for i in range(len(ll)):
            print({ll[i].val}, end=",")
        if ll[0].next == ll[n*-1].next:
            head = head.next
        else:
            ll[0].next = ll[n*-1].next
        return head
        
        
