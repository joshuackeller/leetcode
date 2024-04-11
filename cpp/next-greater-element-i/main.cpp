#include <unordered_map>

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> answers;
        vector<int> stack = {};

        for (int x = 0; x < nums2.size(); x++) {
            while (stack.size() != 0 && stack[stack.size() - 1] < nums2[x]) {
                answers[stack[stack.size() - 1]] = nums2[x];
                stack.pop_back();
            }
            stack.push_back(nums2[x]);
        }

        for (int x = 0; x < nums1.size(); x++) {

            if (answers.find(nums1[x]) != answers.end()) {
                nums1[x] = answers[nums1[x]];
            } else {
                nums1[x] = -1;
            }
        }

        return nums1;
    }
};