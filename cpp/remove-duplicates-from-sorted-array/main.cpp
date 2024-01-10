#include <iostream>
#include <vector>

//  g++ -std=c++11 main.cpp && ./a.out

using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int uniqueIndex = 0;

        vector<int> numsCopy = nums;
        for (int i = 1; i < numsCopy.size(); i++)
        {
            if (nums[uniqueIndex] != numsCopy[i])
            {
                uniqueIndex++;
                nums.insert(nums.begin() + uniqueIndex, numsCopy[i]);
            }
        }

        return uniqueIndex + 1;
    }
};

int main()
{
    Solution solution;

    vector<int> nums = {0, 1, 2, 2, 2, 3, 7, 8, 8, 9};
    cout << solution.removeDuplicates(nums);

    return 0;
}