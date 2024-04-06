pub struct Solution;

// Bottom up / True Dynamic Programming
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut two_back = 0;
        let mut one_back = 1;
        let mut total = 0;

        for _ in 0..n {
            total = one_back + two_back;
            two_back = one_back;
            one_back = total;
        }

        return total;
    }
}

fn main() {
    let result = Solution::climb_stairs(45);
    println!("{}", result);
}
