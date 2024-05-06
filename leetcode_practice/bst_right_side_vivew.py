from collections import deque
from typing import List

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if i == qLen - 1:  # Check if it's the last node at this level
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
