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
    bool isValidBST(TreeNode* root) {

        function<bool(TreeNode*, long,long)> dfs = [&](TreeNode* node, long low, long high){
            if (!node) return true;

            if (!(low < node->val && node->val < high)) return false;


            bool left = dfs(node->left,low,node->val);
            bool right = dfs(node->right,node->val,high);

            return left && right;

        };
        return dfs(root,LONG_MIN,LONG_MAX);
    }
};