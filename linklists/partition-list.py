'''
L86
https://leetcode.com/problems/partition-list/
86. Partition List
Medium
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''
# T: O(n)
# S: O(n)
class Solution:
    def disp(self, head, title=""):
        t = head
        print(f"{title}", end=":")
        while t:
            print(f"{t.val}", end=",")
            t = t.next
            
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        tmp = head
        before, after = None, None
        btail, atail = None, None
        
        # base case
        if tmp is None or tmp.next is None: return tmp
        while tmp is not None:
            # print(f"tmp:{tmp.val}")
            if tmp.val < x:
                if before is None:
                    before = ListNode(tmp.val)
                    btail = before
                else:
                    btail.next = ListNode(tmp.val)
                    btail = btail.next
            else:
                if after is None:
                    after = ListNode(tmp.val)
                    atail = after
                else:
                    atail.next = ListNode(tmp.val)
                    atail = atail.next
            tmp = tmp.next
                    
        # self.disp(before, "bef") 
        # print()
        # self.disp(after, "aft")
        # print()
        if btail and after:
            btail.next = after
        elif btail is None:
            before = after
            
        # self.disp(before, "tot") 
        return before

      
# Optimal solution
# T: O(n)
# S: O(1)
# Did a dummy node initialization at the start to make implementation easier, you don't want that to be part of the returned list,
# hence just move ahead one node in both the lists while combining the two list. Since both before and after have an extra node at the front.
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next
