#include <iostream>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

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
  bool hasPathSum(TreeNode *root, int targetSum) {
    if (root == NULL) {
      return false;
    }
    return testTree(root, targetSum, 0);
  }
  bool testTree(TreeNode *root, int targetSum, int runningSum) {
    int newSum = runningSum + root->val;
    if (root->left == NULL && root->right == NULL && targetSum == newSum) {
      return true;
    }
    if (root->left != NULL && testTree(root->left, targetSum, newSum) == true) {
      return true;
    }
    if (root->right != NULL &&
        testTree(root->right, targetSum, newSum) == true) {
      return true;
    }

    return false;
  }
};

int main() {
  Solution solution;

  TreeNode *root = new TreeNode(5);
  root->left = new TreeNode(4);
  root->left->left = new TreeNode(11);
  root->left->left->left = new TreeNode(7);
  root->left->left->right = new TreeNode(2);

  root->right = new TreeNode(8);
  root->right->left = new TreeNode(13);
  root->right->right = new TreeNode(4);
  root->right->right->right = new TreeNode(1);

  int targetSum = 23;
  bool result = solution.hasPathSum(root, targetSum);

  cout << "RESULT: " << result;

  return 0;
}
