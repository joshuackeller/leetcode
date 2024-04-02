use std::collections::{HashSet, VecDeque};

pub struct Solution;

impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let r_max: usize = grid.len() - 1;
        let c_max: usize = grid[0].len() - 1;

        if grid[0][0] == 1 || grid[r_max][c_max] == 1 {
            return -1;
        }

        let next_options: [[i32; 2]; 8] = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ];

        let mut queue: VecDeque<(usize, usize)> = VecDeque::from([(0, 0)]);
        let mut visited: HashSet<(usize, usize)> = HashSet::from([(0, 0)]);

        let mut size = 0;

        while !queue.is_empty() {
            size += 1;
            let queue_size: usize = queue.len();

            for _ in 0..queue_size {
                if let Some((r, c)) = queue.pop_front() {
                    if r == r_max && c == c_max {
                        return size;
                    }

                    for &[r_diff, c_diff] in &next_options {
                        let r_next: i32 = r as i32 + r_diff;
                        let c_next: i32 = c as i32 + c_diff;

                        if r_next >= 0 && c_next >= 0 {
                            let r_next: usize = r_next as usize;
                            let c_next: usize = c_next as usize;

                            let has_visited = visited.contains(&(r_next, c_next));

                            if r_next <= r_max
                                && c_next <= c_max
                                && !has_visited
                                && grid[r_next][c_next] != 1
                            {
                                queue.push_back((r_next, c_next));
                                visited.insert((r_next, c_next));
                            }
                        }
                    }
                }
            }
        }

        return -1;
    }
}

fn main() {
    let grid = vec![vec![0, 0, 0], vec![1, 1, 0], vec![1, 1, 0]];
    let result = Solution::shortest_path_binary_matrix(grid);

    println!("{}", result);
}
