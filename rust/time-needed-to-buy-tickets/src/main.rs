use std::cmp::min;

pub struct Solution;

impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let t = tickets[k as usize];
        let mut count = t;
        for x in 0..tickets.len() {
            if x < k as usize {
                count += min(tickets[x], t);
            } else if x > k as usize {
                count += min(tickets[x], t - 1);
            }
        }

        return count;
    }
}

fn main() {
    println!("Hello, world!");
}
