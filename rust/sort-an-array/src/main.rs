use std::time::Instant;

fn main() {
    // #4 - Counting Sort
    // Fastest for a leetcode challenge, but not realistic for real-world scenarios
    // 1. Basically has a fixed time it takes to run (about 1.5 - 3 seconds) - won't run faster for
    //    smaller (more common arrays)
    // 2. In a real-world scenario you won't know how large your number will be (in the leet code
    //    challanege we know it will be between -100,000 and 100,000). To implement this in the
    //    real world, you'd have to make a massive nums_array, which would decrease the performance
    //    of the function
    // pub fn sort_array(mut nums: Vec<i32>) -> Vec<i32> {
    //     let mut nums_array: [i32; 100_001] = [0; 100_001];

    //     for x in nums.iter() {
    //         let adjusted_x = x + 50_000;
    //         nums_array[adjusted_x as usize] += 1;
    //     }

    //     let mut index: usize = 0;
    //     for x in 0..100_001 {
    //         for _ in 0..nums_array[x] {
    //             nums[index] = (x - 50_000) as i32;
    //             index += 1;
    //         }
    //     }

    //     return nums;
    // }

    // #3 - Merge sort
    fn merge_array(nums: &mut Vec<i32>, start: usize, end: usize) {
        if end - start <= 0 {
            return;
        }
        let middle: usize = (end - start) / 2 + start;

        merge_array(nums, start, middle);
        merge_array(nums, middle + 1, end);

        merge(nums, start, middle, end);
    }

    fn merge(nums: &mut Vec<i32>, start: usize, middle: usize, end: usize) {
        let vec_a = nums[start..=middle].to_vec();
        let vec_b = nums[(middle + 1)..=end].to_vec();
        let mut a = 0;
        let a_max = middle - start;
        let mut b = 0;
        let b_max = end - middle - 1;

        for x in start..=end {
            if a > a_max {
                nums[x] = vec_b[b];
                b += 1;
            } else if b > b_max {
                nums[x] = vec_a[a];
                a += 1;
            } else {
                if vec_a[a] < vec_b[b] {
                    nums[x] = vec_a[a];
                    a += 1;
                } else {
                    nums[x] = vec_b[b];
                    b += 1;
                }
            }
        }
    }

    fn sort_array(mut nums: Vec<i32>) -> Vec<i32> {
        let end = nums.len() - 1;
        merge_array(&mut nums, 0, end);
        return nums;
    }

    // #2 - SLOWER INSERT METHOD
    // let mut new_vec: Vec<i32> = nums.clone();
    // for (i, num) in new_vec.clone().iter().enumerate().skip(1) {
    //     let mut x: i32 = i as i32 - 1;
    //     while x >= 0 && num < &new_vec[x as usize] {
    //         let temp = *num;
    //         new_vec[x as usize + 1] = new_vec[x as usize];
    //         new_vec[x as usize] = temp;
    //         x = x - 1;
    //     }
    // }
    // return new_vec;

    // #1 - OG - pretty much same as insert method, just a little faster
    // let mut new_vec: Vec<i32> = nums.clone();
    // for num in nums.iter() {
    //     if new_vec.len() < 1 {
    //         new_vec.push(*num);
    //     } else if num >= &new_vec[new_vec.len() - 1] {
    //         new_vec.push(*num);
    //     } else if num <= &new_vec[0] {
    //         new_vec.insert(0, *num);
    //     } else {
    //         for (index, new_num) in new_vec.clone().iter().enumerate() {
    //             if new_num > num {
    //                 new_vec.insert(index, *num);
    //                 break;
    //             }
    //         }
    //     }
    // }
    //return new_vec;

    // Start the timer
    let start_time = Instant::now();

    let vector: Vec<i32> = vec![5, 3, 4, 2, 1];
    sort_array(vector);

    // Stop the timer
    let end_time = Instant::now();

    // Calculate the elapsed time
    let elapsed_time = end_time - start_time;

    // Output the elapsed time
    println!("Finished 🐌: {:?}", elapsed_time);

    // for num in results.iter() {
    //     println!("{}", num);
    // }
}
