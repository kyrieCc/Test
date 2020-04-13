'''
(2)
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
例1：
        输入： root = [3,1,4,null,2], k = 1
        输出：1
        说明：3为根节点； 3的左节点为1，右节点为4；1的左节点为空，右节点为2；4为叶子节点。
例2：
        输入：root = [5,3,6,2,4,null,null,1], k = 3
        输出：3
说明：5为根节点； 5的左节点为3，右节点为6；3的左节点为2，右节点为4；2的左节点为1，右节点为空；1,4,6为叶子节点。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root :
            return
        curL = [root]
        res = []
        while curL:
            nextL = []
            tmp =[]
            for node in curL:
                tmp.append(node.val)
                if node.left:
                    nextL.append(node.left)
                if node.right:
                    nextL.append(node.right)
            res.extend(tmp)
            curL = nextL
            res = sorted(res)
        return res[k-1]
if __name__ == '__main__':
    head = TreeNode(3)
    head.left = TreeNode(1)
    head.right = TreeNode(4)
    head.right.right = TreeNode(2)
    a = Solution()
    print(a.kthSmallest(head,1))


