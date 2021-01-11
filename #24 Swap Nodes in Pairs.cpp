/*
Given a linked list, swap every two adjacent nodes and return its head.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
 

Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
*/


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *p = head;
        ListNode *last = new ListNode();
        if (head && head -> next)
            head = head -> next;  // non-empty linked list starts with node 2
        else
            return head;
        while (p && p -> next){
            ListNode *q = p -> next;
            last -> next = q;
            p -> next = q -> next;
            q -> next = p;
            last = p;
            p = p -> next;
        }
        return head;
    }
};