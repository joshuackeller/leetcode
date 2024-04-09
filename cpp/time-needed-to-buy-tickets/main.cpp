#include <vector>

using namespace std;

class Solution {
public:
  int timeRequiredToBuy(vector<int> &tickets, int k) {
    int t = tickets[k];
    int count = t;
    for (int x = 0; x < tickets.size(); x++) {
      if (x < k) {
        count += min(tickets[x], t);
      } else if (x > k) {
        count += min(tickets[x], t - 1);
      }
    }

    return count;
  }
};
