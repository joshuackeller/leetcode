pub struct Solution;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let row: usize = m as usize;
        let col: usize = n as usize;

        let mut grid: Vec<Vec<i32>> = vec![vec![1; col]; row];

        for r in 1..row {
            for c in 1..col {
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1];
            }
        }

        return grid[row - 1][col - 1];
    }
}

fn main() {
    let result = Solution::unique_paths(3, 7);
    println!("{}", result);
}
