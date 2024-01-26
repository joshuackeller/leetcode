fn main() {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut scores: Vec<i32> = vec![];

        for operation in operations {
            if operation == "+" {
                scores.push(scores[scores.len() - 1] + scores[scores.len() - 2]);
            } else if operation == "D" {
                scores.push(2 * scores[scores.len() - 1]);
            } else if operation == "C" {
                scores.remove(scores.len() - 1);
            } else {
                scores.push(operation.parse::<i32>().unwrap());
            }
        }

        return scores.iter().sum();
    }

    let string_vector: Vec<String> = vec!["5", "-2", "4", "C", "D", "9", "+", "+"]
        .iter()
        .map(|s| s.to_string())
        .collect();
    let result = cal_points(string_vector);

    println!("{}", result);
}
