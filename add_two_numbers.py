# https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def disp(self, s:ListNode, msg='disp'):
        print(msg, end=':')
        n = s
        while n:
            print(n.val, end=' ')
            n = n.next
        print('')
        
    def add_stack(self, val, ll:ListNode):
        t = ListNode(val)    
        if ll is None:
            ll = t
        else:
            t.next = ll
            ll = t
        return ll

    def add(self, val, ll:ListNode):
        n = ListNode(val)
        t = ll
        if t is None:
            # print("inited list")
            ll = n
        else:
            while t.next:
                t = t.next
            t.next = n
        return ll

    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tot = 0
        carry = 0
        l3 = None

        while l1 or l2:
            if l1 == None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 == None:
                l2_val = 0
            else:
                l2_val = l2.val
            tot = l1_val + l2_val + carry
            # print(f"{l1_val} + {l2_val} + <{carry}> = {tot}")            
            if tot >= 10:
                carry = 1
                tot -= 10
            else:
                carry = 0
            # print(f"carry:{carry} storing {tot}")
            l3 = self.add(tot, l3)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            # print(f"carry:{carry}->storing")
            l3 = self.add(carry, l3)
        return l3
