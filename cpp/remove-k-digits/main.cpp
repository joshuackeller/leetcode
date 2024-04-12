class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<int> nums = {};

        for (int x = 0; x < num.length(); x++) {
            nums.push_back(num[x] - '0');
        }

        vector<int> stack = {};
        int removalCount = 0;
        for (int x = 0; x < nums.size(); x++) {
            while (stack.size() != 0 && removalCount < k &&
                   stack[stack.size() - 1] > nums[x]) {
                stack.pop_back();
                removalCount++;
            }
            stack.push_back(nums[x]);
        }

        while (removalCount < k) {
            stack.pop_back();
            removalCount++;
        }

        string answer = "";
        for (int x = 0; x < stack.size(); x++) {
            if (stack[x] != 0 || answer != "") {
                answer.append(to_string(stack[x]));
            }
        }

        if (answer == "") {
            return "0";
        } else {
            return answer;
        }
    }
};