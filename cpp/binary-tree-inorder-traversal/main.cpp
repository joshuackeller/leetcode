#include <iostream>
#include <vector>

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
  vector<int> inorderTraversal(TreeNode *root) {
    vector<int> order;

    if (root == NULL) {
      return order;
    }

    vector<int> left = inorderTraversal(root->left);
    order.insert(order.end(), left.begin(), left.end());

    order.push_back(root->val);

    vector<int> right = inorderTraversal(root->right);
    order.insert(order.end(), right.begin(), right.end());

    return order;
  }
};

int main() {

  Solution solution;

  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right = new TreeNode(3);
  root->right->right = new TreeNode(6);

  vector<int> result = solution.inorderTraversal(root);

  cout << "\n ANSWER: ";
  // Expected result: 4, 2, 5, 1, 3, 6.
  for (int x = 0; x < result.size(); x++) {
    cout << result[x] << ", ";
  }

  return 0;
}
