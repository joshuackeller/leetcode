
#include <vector>
using namespace std;

class Solution {
public:
  int minCostClimbingStairs(vector<int> &cost) {
    if (cost.size() == 1) {
      return cost[0];
    } else {

      int twoBack = cost[0];
      int oneBack = cost[1];
      int total = 0;

      for (int x = 2; x < cost.size(); x++) {
        total = cost[x] + min(oneBack, twoBack);
        twoBack = oneBack;
        oneBack = total;
      }

      return min(oneBack, twoBack);
    }
  }
};
