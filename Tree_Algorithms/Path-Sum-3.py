# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        rst = []
        lis = self.preorder(root)
        for i in lis:
            self.dfs(i, sum, rst, [])
        return len(rst)
    def dfs(self,root, sum,rst, path):
        if not root:
            return
        path.append(root.val)
        if self.summation(path) == sum:
            rst.append(path[:])
        self.dfs(root.left, sum,rst,path)
        self.dfs(root.right, sum ,rst,path)
        path.pop()
    def summation(self,lis):
        return sum(lis)
    def preorder(self,root):
        ans = []
        stack = [root]
        while stack:
            curr = stack.pop()
            ans.append(curr)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans

# Just have to find number of paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        rst = []
        ans = 0
        lis = self.preorder(root)
        for i in lis:
            self.dfs(i, sum, rst, [])
        return len(rst)
    def dfs(self,root, sum,rst, path):
        if not root:
            return
        path.append(root.val)
        if self.summation(path) == sum:
            rst.append(1)
        self.dfs(root.left, sum,rst,path)
        self.dfs(root.right, sum ,rst,path)
        path.pop()
    def summation(self,lis):
        return sum(lis)
    def preorder(self,root):
        ans = []
        stack = [root]
        while stack:
            curr = stack.pop()
            ans.append(curr)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans

class Solution3:
    count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        ans = 0
        lis = self.preorder(root)
        for i in lis:
            self.dfs(i, sum, self.count, [])
        return self.count
    def dfs(self,root, sum,rst, path):
        if not root:
            return
        path.append(root.val)
        if self.summation(path) == sum:
            self.count+=1
        self.dfs(root.left, sum,self.count,path)
        self.dfs(root.right, sum ,self.count,path)
        path.pop()
    def summation(self,lis):
        return sum(lis)
    def preorder(self,root):
        ans = []
        stack = [root]
        while stack:
            curr = stack.pop()
            ans.append(curr)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution4:
    count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def pathSum_a(root,sum):
            if root == None:
                return 0
            res = 0
            if root.val == sum:
                res+=1
            res+=pathSum_a(root.left, sum-root.val)
            res+=pathSum_a(root.right, sum-root.val)
            return res
        if root == None:
            return 0
        return self.pathSum(root.left,sum) + pathSum_a(root, sum) + self.pathSum(root.right,sum)
                
                
            
            
        
    
            
        
    
    