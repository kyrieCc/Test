#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        curLayer = [pRoot]
        res = []
        cnt = 0
        while curLayer:
            nextLayer = []
            tmp = []
            for node in curLayer:
                tmp.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            if cnt == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            curLayer = nextLayer
            cnt = (cnt+1) % 2
        return res
if __name__ == '__main__':
    head = TreeNode("a")
    head.left = TreeNode("b")
    head.right = TreeNode("c")
    head.left.left = TreeNode("d")
    head.right.right = TreeNode("e")
    a = Solution()
    print(a.Print(head))

