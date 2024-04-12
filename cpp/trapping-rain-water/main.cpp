#include <vector>

using namespace std;

class Solution {
public:
  int trap(vector<int> &height) {
    int l = 0;
    int r = height.size() - 1;
    int lMax = height[l];
    int rMax = height[r];
    int water = 0;

    while (l < r) {
      if (lMax < rMax) {
        water += max(lMax - height[l], 0);
        l++;
        lMax = max(lMax, height[l]);
      } else {
        water += max(rMax - height[r], 0);
        r--;
        rMax = max(rMax, height[r]);
      }
    }

    return water;
  }
};

// class Solution {
// public:
//     int trap(vector<int>& height) {
//         vector<int> stack = {};
//         int water = 0;

//         for (int x = 0; x < height.size(); x++) {
//             if (stack.size() > 0 && stack.back() < height[x]) {
//                 int currentLimit = min(height[x], stack[0]);
//                 for (int y = stack.size() - 1; y >= 0; y--) {
//                     water += max(currentLimit - stack[y], 0);
//                     if (height[x] > stack[0]) {
//                         stack.pop_back();
//                     } else {
//                         stack[y] = max(currentLimit, stack[y]);
//                     }
//                 }
//             }
//             stack.push_back(height[x]);
//         }

//         return water;
//     }
// };