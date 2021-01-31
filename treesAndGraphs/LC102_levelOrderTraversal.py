# https://www.youtube.com/watch?v=MBZ-gBkjdMc&ab_channel=DEEPTITALESRA
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        nums = [root]
        nextTree = []
        valsAtLevel = []

        while nums:             
            for num in nums:
                valsAtLevel.append(num.val)
                if num.left:
                    nextTree.append(num.left)
                if num.right:
                    nextTree.append(num.right)

            res.append(valsAtLevel)
            valsAtLevel = []
            nums = nextTree
            nextTree = []

        return res
        