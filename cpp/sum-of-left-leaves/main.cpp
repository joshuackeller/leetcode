/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        int count = 0;
        if(root->left != NULL) {
            count += sumOfLeftLeaves(root->left);
        } 
        if(root->right != NULL) {
            count += sumOfLeftLeaves(root->right);
        }

        if(root->left != NULL && root->left->left == NULL && root->left->right == NULL) {
            return root->left->val + count;
        } else {
            return count;
        }
    }
    
};