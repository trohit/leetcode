"""
L206
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List
Easy
Given the head of a singly linked list, reverse the list, and return the reversed list. 

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints: The number of nodes in the list is the range [0, 5000]. 
-5000 <= Node.val <= 5000 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # need 3 ptr dance : p, c, n
        p = None
        c = head
        n = None
        while c:
            n = c.next  # store next
            c.next = p  # make next point to prev 
            p = c       # slide prev ptr to curr
            c = n       # slide curr ptr to next
        head = p # this is the new head
        return head
"""
test cases
boundary conditions:
len : 0 , 1 , 2 , 3
"""
