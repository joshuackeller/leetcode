fn main() {
    fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut count = 0;

        for num in nums.clone().iter() {
            if num != &val {
                nums[count] = *num;
                count += 1;
            }
        }

        return count as i32;
    }

    let result = remove_element(&mut vec![0, 1, 2, 2, 3, 0, 4, 2], 2);

    println!("{}", result)
}
