use std::collections::BinaryHeap;

pub struct Solution;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::from(stones);

        while let Some(y) = heap.pop() {
            if let Some(x) = heap.pop() {
                if x < y {
                    heap.push(y - x);
                }
            } else {
                return y;
            }
        }

        return 0;
    }
}

fn main() {
    let stones = vec![7, 6, 7, 6, 9];
    //  let stones = vec![2, 7, 4, 1, 8, 1];

    let answer = Solution::last_stone_weight(stones);

    println!("{}", answer);
}
