class Solution:
    res = -9999999
    def helper(self, root: TreeNode):
        if root == None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        MS = max(max(left,right)+root.val, root.val)
        M21 = max(MS, left+right+root.val)
        self.res = max(M21, self.res)
        return MS
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.res