fn main() {
    fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut nums_copy = nums.clone();
        for num in nums.iter() {
            nums_copy.push(*num)
        }
        return nums_copy;
    }

    let string_vector: Vec<i32> = vec![1, 2, 3, 1];

    let result = get_concatenation(string_vector);

    println!("{:?}", result);
}
