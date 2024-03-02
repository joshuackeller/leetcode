fn main() {
    for x in 1000..=2499 {
        let x_reverse_string = x.to_string().chars().rev().collect::<String>();
        let y_string = (x * 4).to_string();
        if x_reverse_string == y_string {
            println!("{}", x);
        }
    }
}
