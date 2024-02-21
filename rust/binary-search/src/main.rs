fn main() {
    fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;

        // Not necessary, but makes it slightly faster for large cases
        if nums[right] < target || nums[left] > target {
            return -1;
        }

        while left <= right {
            let middle = (left + right) / 2;

            // Not necessary, but makes it slightly faster for large cases
            if nums[left] == target {
                return left as i32;
            }
            if nums[right] == target {
                return right as i32;
            }

            if nums[middle] < target {
                left = middle + 1;
            } else if nums[middle] > target {
                if middle == 0 {
                    return -1;
                }
                right = middle - 1;
            } else {
                return middle as i32;
            }
        }

        return -1;
    }

    let nums: Vec<i32> = vec![
        -8, -7, -6, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    ];
    let target: i32 = 19;
    let result = search(nums, target);

    println!("{}", result);
}
