use std::cmp::max;

pub struct Solution;

impl Solution {
    pub fn rob(mut nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        } else if nums.len() > 2 {
            nums[2] = nums[2] + nums[0];

            for x in 3..nums.len() {
                nums[x] = nums[x] + max(nums[x - 2], nums[x - 3]);
            }
        }

        return max(nums[nums.len() - 1], nums[nums.len() - 2]);
    }
}

fn main() {
    let nums: Vec<i32> = vec![1, 3, 4, 7, 2, 1, 9];

    let result = Solution::rob(nums);

    println!("\n {}", result);
}
