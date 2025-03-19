from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty
        if not p and not q:
            return True
        # If one of them are empty, not both
        if not p or not q:
            return False
        # If both trees value is not equal
        if p.val != q.val:
            return False

        # Checking both trees left and right nodes and length are equal or not
        return issubclass(p.left, q.left) and issubclass(p.right, q.right)