pub struct Solution;

impl Solution {
    pub fn hamming_weight(mut n: i32) -> i32 {
        let mut count: i32 = 0;
        while n > 0 {
            if n & 1 == 1 {
                count += 1;
            }
            n = n >> 1;
        }

        return count;
    }
}

fn main() {
    let result: i32 = Solution::hamming_weight(11);
    println!("{}", result);
}
