"""
https://leetcode.com/problems/merge-k-sorted-lists/
23. Merge k Sorted Lists
Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ll = lists
        hl = [] # heap list
        rl = ListNode(-1) # result list
        fl = rl # follow list to result list
        for cl in ll: # k lists , so O(k * e) = O(N)
            while cl: # e elms each 
                hl.append(cl.val)
                cl = cl.next
        while hl: # N times so N log N where N is tot # nodes in final list
            v = heapq.heappop(hl) # Pop a value O(logN)
            fl.next = ListNode(v)
            fl = fl.next
        return rl.next
        # O(N) + O(N*logN) => O(N*logN)
        
