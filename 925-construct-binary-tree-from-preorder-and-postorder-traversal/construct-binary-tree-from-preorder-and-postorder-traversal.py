# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # read this: https://www.techiedelight.com/construct-full-binary-tree-from-preorder-postorder-sequence/
        def helper(pre,post):
            print('pre is: ', pre, 'post is: ', post)
            if not pre:
                return None
        
            if len(pre)==1:
                return TreeNode(post.pop())
        
        
            node=TreeNode(post.pop()) #3
            ind=pre.index(post[-1]) #4
        
            node.right=helper(pre[ind:],post) #1
            node.left=helper(pre[1:ind],post) #2
            return node
    
        return helper(pre,post)