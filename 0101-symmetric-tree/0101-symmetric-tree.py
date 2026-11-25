# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        def is_symetric(left_node, right_node):
            # 1. Both sides hit a end (None)
            if not left_node and not right_node:
                return True

            # Only one side is None or values dosent matched
            if (left_node and not right_node) or (not left_node and right_node) or (left_node.val != right_node.val):
                return False
            
            #check outer and inner mirror symmetric now, compare outer edges & inner edges
            return is_symetric(left_node.left, right_node.right) and is_symetric(left_node.right, right_node.left)

        #return the left and right compare.
        return is_symetric(root.left, root.right)
