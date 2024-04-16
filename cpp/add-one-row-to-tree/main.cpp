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

// SOLUTION #2: BFS
class Solution {
public:
  TreeNode *addOneRow(TreeNode *root, int val, int depth) {
    if (depth == 1) {
      return new TreeNode(val, root, NULL);
    }

    int currentDepth = 1;
    queue<TreeNode *> q;

    q.push(root);

    while (!q.empty()) {
      currentDepth++;
      int size = q.size();

      for (int x = 0; x < size; x++) {
        TreeNode *node = q.front();
        q.pop();

        if (currentDepth == depth) {
          node->left = new TreeNode(val, node->left, NULL);
          node->right = new TreeNode(val, NULL, node->right);
        } else {
          if (node->left != NULL) {
            q.push(node->left);
          }
          if (node->right != NULL) {
            q.push(node->right);
          }
        }
      }
    }

    return root;
  }
};

// SOLUTION #1: Recursive
// class Solution {
// public:
//     TreeNode* addOneRow(TreeNode* root, int val, int depth) {
//         if (depth == 1) {
//             TreeNode* newTree = new TreeNode(val, root, NULL);
//             return newTree;
//         } else {
//         int currentDepth = 1;
//         return solve(root, val, depth, currentDepth);
//         }

//     }
//     TreeNode* solve(TreeNode* root, int val, int depth, int currentDepth) {
//         TreeNode* newTree = new TreeNode(root->val);
//         currentDepth++;

//         if (depth == currentDepth) {
//             newTree->left = new TreeNode(val, root->left, NULL);
//             newTree->right = new TreeNode(val, NULL, root->right);\
//             return newTree;
//         }

//         if (root->left != NULL) {
//             newTree->left = solve(root->left, val, depth, currentDepth);
//         }
//         if (root->right != NULL) {
//             newTree->right = solve(root->right, val, depth, currentDepth);
//         }

//         return newTree;
//     }
// };
