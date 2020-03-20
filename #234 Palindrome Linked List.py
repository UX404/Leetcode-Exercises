'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''


# 1 Basic method
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        for n in range(int(len(ls) / 2)):
            if ls[n] != ls[len(ls)-n-1]: return False
        return True


# 2 Reverse first half, space o(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        if not head.next: return True
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        lh = int((length - 2) / 2)
        rh = int((length + 1) / 2)

        p = head
        q = head.next
        p.next = None
        for n in range(lh):
            r = q.next
            q.next = p
            p = q
            q = r
        lhnode = p
        if rh == lh + 1:
            rhnode = q
        else:
            rhnode = q.next
        # Reverse the fist half

        while rhnode:
            if lhnode.val != rhnode.val: return False
            lhnode = lhnode.next
            rhnode = rhnode.next
        return True