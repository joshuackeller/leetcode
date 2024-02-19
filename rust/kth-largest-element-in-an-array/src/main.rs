use std::collections::BinaryHeap;
use std::time::Instant;

fn main() {
    // #1 - This works unless you're doing one of leetcodes stupid test cases
    // fn quick_select(nums: &mut Vec<i32>, start: usize, end: usize, kth_index: usize) {
    //     if end - start <= 0 {
    //         return;
    //     }

    //     let pivot_index = thread_rng().gen_range(start..=end);
    //     let pivot = nums[pivot_index];
    //     nums.swap(pivot_index, end);

    //     let mut left = start;
    //     for index in start..=end {
    //         if nums[index] < pivot {
    //             nums.swap(left, index);
    //             left += 1;
    //         }
    //     }

    //     nums.swap(left, end);

    //     if left == kth_index {
    //         return;
    //     } else if left > kth_index {
    //         if left >= 1 && left - start > 0 {
    //             quick_select(nums, start, left - 1, kth_index);
    //         }
    //     } else {
    //         if end - start > 0 {
    //             quick_select(nums, left + 1, end, kth_index);
    //         }
    //     }
    // }

    // fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
    //     let end = nums.len() - 1;
    //     let kth_index = nums.len() - k as usize;
    //     quick_select(&mut nums, 0, end, kth_index);

    //     return nums[nums.len() - k as usize];
    // }

    // # 2 - Heap
    fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut heap = BinaryHeap::from(nums);

        for _ in 0..(k - 1) {
            heap.pop();
        }

        return *heap.peek().unwrap();
    }

    let start_time = Instant::now();

    let nums = vec![-6, 2, 4, 1, 3];
    let k = 1;
    let result = find_kth_largest(nums, k);

    let end_time = Instant::now();

    let elapsed_time = end_time - start_time;
    println!("Finished 🐌: {:?}", elapsed_time);

    println!("{}", result);
}
