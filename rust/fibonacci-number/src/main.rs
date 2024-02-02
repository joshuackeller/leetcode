fn main() {
    pub fn fib(n: i32) -> i32 {
        let mut first: i32 = 0;
        let mut second: i32 = 1;
        let mut count: i32 = 0;

        if n == 0 {
            return 0;
        } else if n == 1 {
            return 1;
        }

        while count < n - 1 {
            let previous_second = second;
            second = second + first;
            first = previous_second;
            count += 1;
        }

        return second;
    }

    let answer = fib(30);

    println!("{}", answer);
}

// 0
// 1
// 1
// 2
// 3
