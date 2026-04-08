class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        curr = root
        q = deque()
        if root:
            q.append(root)
        res = []

        while q:
            qLen = len(q)
            lvl = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
            if lvl:
                res.append(lvl)
        
        return res