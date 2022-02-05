'''
https://leetcode.com/problems/middle-of-the-linked-list/
876. Middle of the Linked List
Easy
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Runtime: 32 ms, faster than 70.37% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 96.90% of Python3 online submissions for Middle of the Linked List.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        while f:
            # print(f"s:{s.val}, f:{f.val}")
            if f and f.next:
                f = f.next.next
                s = s.next
            else:
                break
        # print(f"end s:{s.val}")
        return s            
        
