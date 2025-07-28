#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (43.23%)
# Likes:    12936
# Dislikes: 1937
# Total Accepted:    1.4M
# Total Submissions: 3.2M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        valid_words: set[str] = set(wordList)
        valid_chars: dict[int, set[str]] = defaultdict(lambda: set())
        if endWord not in valid_words:
            return 0

        for i, ith_valid_chars in enumerate([pos for pos in zip(*wordList)]):
            valid_chars[i].update(ith_valid_chars)

        bfs_queue: deque[tuple[str, int]] = deque()
        bfs_queue.append((beginWord, 1))
        while len(bfs_queue):
            word, current_step = bfs_queue.popleft()
            if word == endWord:
                return current_step
            for i, char in enumerate(word):
                for valid_char in valid_chars.get(i, []):
                    if valid_char == char:
                        continue
                    word_candidate = f"{word[0:i]}{valid_char}{word[i + 1 :]}"
                    if word_candidate in valid_words:
                        valid_words.remove(word_candidate)
                        bfs_queue.append((word_candidate, current_step + 1))
        return 0


# @lc code=end
