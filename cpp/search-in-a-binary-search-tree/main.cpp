#include <iostream>

using namespace std;

//  g++ -std=c++11 main.cpp && ./a.out
//
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  TreeNode *searchBST(TreeNode *root, int val) {
    while (root != NULL) {
      if (root->val < val) {
        root = root->right;
      } else if (root->val > val) {
        root = root->left;
      } else {
        return root;
      }
    }
    return NULL;
  }
};

int main() {

  Solution solution;

  TreeNode *root = new TreeNode(5);
  root->left = new TreeNode(4);
  root->left->left = new TreeNode(3);
  root->right = new TreeNode(6);
  root->right->right = new TreeNode(7);

  int val = 6;

  TreeNode *result = solution.searchBST(root, val);

  cout << result->val << "\n";

  return 0;
}
