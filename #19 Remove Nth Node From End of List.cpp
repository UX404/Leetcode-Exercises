/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
*/


class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *nodes[30] = {nullptr};
        ListNode *p = head;
        int i = 0;
        while (p){
            nodes[i] = p;
            i ++;
            p = p -> next;
        }
        
        if (i == n)
            return nodes[1];
        else{
            nodes[i-n-1] -> next = nodes[i-n+1];
            return nodes[0];
        }
    }
};