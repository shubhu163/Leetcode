/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxAncestorDiff(TreeNode* root) {
        function<int(TreeNode*,int,int)> dfs = [&](TreeNode* node, int mn, int mx){
            if (!node) return mx - mn;

            mx = max(mx,node->val);
            mn = min(mn,node->val);

            int left = dfs(node->left,mn,mx);
            int right = dfs(node->right,mn,mx);

            return max(left,right);

        };

        return dfs(root,root->val,root->val);


    }
};

