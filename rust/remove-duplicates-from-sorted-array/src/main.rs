fn main() {
    fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut unique_index: i32 = 0;

        for (index, n) in nums.clone().iter().enumerate() {
            if index == 0 {
                continue;
            }
            if n != &nums[unique_index as usize] {
                unique_index += 1;
                nums.insert(unique_index as usize, *n);
            }
        }

        return unique_index + 1;
    }

    let mut nums = vec![0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 8];
    let result = remove_duplicates(&mut nums);

    println!("{}", result)
}
