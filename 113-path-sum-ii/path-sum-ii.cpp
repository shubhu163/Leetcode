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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int>path;

        function<void(TreeNode* ,long)> dfs = [&](TreeNode* node, long rem){
            if (!node) return;

            path.push_back(node->val);
            rem += node->val;
            
            if (!node->left and !node->right and rem==targetSum) result.push_back(path);
            dfs(node->left,rem);
            dfs(node->right,rem);
            path.pop_back();

        };
        dfs(root,0);
        return result;
        
    }
};


