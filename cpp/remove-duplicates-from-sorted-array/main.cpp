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

        int size = nums.size();
        for (int i = 1; i < size; i++)
        {
            if (nums[uniqueIndex] != nums[i])
            {
                uniqueIndex++;
                nums[uniqueIndex] = nums[i];
            }
        }

        cout << "start\n";
        for (int i = 0; i < nums.size(); i++)
        {
            cout << nums[i] << "\n";
        }
        cout << "end\n";

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