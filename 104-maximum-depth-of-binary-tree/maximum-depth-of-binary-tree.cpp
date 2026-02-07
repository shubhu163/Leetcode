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
    int maxDepth(TreeNode* root) {

        function<int(TreeNode*, int)>dfs = [&](TreeNode* node, int count){
            if (!node) return count;

            count += 1;
            int left = dfs(node->left,count);
            int right = dfs(node->right,count);

            return max(left,right);
        };
        return dfs(root,0);
    

        
    }
};