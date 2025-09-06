"""
Find length of Loop
    - https://www.geeksforgeeks.org/problems/find-length-of-loop/1
Difficulty: Medium
Accuracy: 44.26%
Submissions: 279K+
Points: 4
Average Time: 30m

Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

Examples:

Input: pos = 2,
   
Output: 4
Explanation: There exists a loop in the linked list and the length of the loop is 4.

Input: pos = 3,
   
Output: 3
Explanation: The loop is from 19 to 10. So length of loop is 19 → 33 → 10 = 3.

Input: pos = 0,
    
Output: 0
Explanation: There is no loop.

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 104
0 ≤ pos < number of nodes
"""

'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

from collections import defaultdict

class Solution:
    def lengthOfLoop(self, head):
        loop_node = head
        visited = defaultdict(int)
        counter = 0
        while loop_node is not None:
            counter+=1
            if visited.get(loop_node, 0):
                return counter-visited[loop_node]
            visited[loop_node] = counter
            loop_node = loop_node.next
        return 0
                       

    def fast_slow_lengthOfLoop(self, head):
        fast, node = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            node = node.next
            if fast == node:
                break
        else:
            return 0
        counter = 1
        fast = fast.next
        while fast != node:
            counter += 1
            fast = fast.next

        return counter