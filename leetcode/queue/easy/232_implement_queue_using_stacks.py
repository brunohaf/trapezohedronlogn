#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (65.20%)
# Likes:    10890
# Dislikes: 1047
# Total Accepted:    1.4M
# Total Submissions: 2.1M
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).
#
# Implement the MyQueue class:

#     void push(int x) Pushes element x to the back of the queue.
#     int pop() Removes the element from the front of the queue and returns it.
#     int peek() Returns the element at the front of the queue.
#     boolean empty() Returns true if the queue is empty, false otherwise.
#
# Notes:
#     You must use only standard operations of a stack, which means only push
#     to top, peek/pop from top, size, and is empty operations are valid.
#     Depending on your language, the stack may not be supported natively. You
#     may simulate a stack using a list or deque (double-ended queue) as long
#     as you use only a stack's standard operations.
#
#
# Example 1:
#
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
#
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1,2] (leftmost is front of the queue)
# myQueue.peek();  // return 1
# myQueue.pop();   // return 1, queue is [2]
# myQueue.empty(); // return false
#
#
# Constraints:
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
#
#
# Follow-up:
# Can you implement the queue such that each operation is amortized O(1) time
# complexity? In other words, performing n operations will take overall O(n)
# time even if one of those operations may take longer.


# @lc code=start
from collections import deque


class MyQueue:
    aux_stack: deque
    queue_stack: deque

    def __init__(self) -> None:
        self.queue_stack = deque()
        self.aux_stack = deque()

    def push(self, x: int) -> None:
        if not len(self.queue_stack):
            self.queue_stack.append(x)
            return

        while len(self.queue_stack):  # O(n) + O(n)
            self.aux_stack.append(self.queue_stack.pop())

        self.aux_stack.append(x)

        while len(self.aux_stack):
            self.queue_stack.append(self.aux_stack.pop())
        return

    def pop(self) -> int:  # O(1)
        return self.queue_stack.pop()

    def peek(self) -> int:  # O(1)
        if len(self.queue_stack) > 0:
            return self.queue_stack[-1]
        raise Exception("The queue is empty")

    def empty(self) -> bool:  # O(1)
        return len(self.queue_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# @lc code=end

"""
myQueue: MyQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1,2] (leftmost is front of the queue)
print(myQueue.peek())  # return 1
print(myQueue.pop())  # return 1, queue is [2]
print(myQueue.empty())  # return false
"""
