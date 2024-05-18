class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            left_val = dfs(node.left)
            right_val = dfs(node.right)

            self.moves += abs(left_val) + abs(right_val)

            total_val = node.val + left_val + right_val
            return total_val - 1

        dfs(root)
        return self.moves