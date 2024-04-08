use std::collections::VecDeque;

pub struct Solution;

impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut st_square: i32 = students.iter().filter(|&s| *s == 1).count() as i32;
        let mut st_circle: i32 = students.len() as i32 - st_square;

        let mut current_sa = 0;

        for _ in 0..students.len() {
            if sandwiches[current_sa] == 1 && st_square == 0 {
                return st_circle;
            } else if sandwiches[current_sa] == 0 && st_circle == 0 {
                return st_square;
            }
            if sandwiches[current_sa] == 1 {
                st_square -= 1;
            } else {
                st_circle -= 1;
            }
            current_sa += 1;
        }

        return 0;
    }
}

fn main() {
    let students = vec![1, 1, 1, 0, 0, 1];
    let sandwiches = vec![1, 0, 0, 0, 1, 1];
    let result = Solution::count_students(students, sandwiches);
    println!("result: {}", result);
}

// impl Solution {
//     pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
//         let mut st_square: i32 = students.iter().filter(|&s| *s == 1).count() as i32;
//         let mut st_circle: i32 = students.len() as i32 - st_square;
//
//         let mut queue: VecDeque<i32> = VecDeque::from(students);
//
//         let mut current_sa = 0;
//
//         while !queue.is_empty() {
//             let current_st = queue.pop_front().unwrap();
//
//             if current_st == sandwiches[current_sa] {
//                 current_sa += 1;
//                 if current_st == 1 {
//                     st_square -= 1;
//                 } else {
//                     st_circle -= 1;
//                 }
//             } else {
//                 queue.push_back(current_st);
//                 if sandwiches[current_sa] == 1 && st_square == 0 {
//                     return st_circle;
//                 } else if sandwiches[current_sa] == 0 && st_circle == 0 {
//                     return st_square;
//                 }
//             }
//         }
//
//         return 0;
//     }
// }
