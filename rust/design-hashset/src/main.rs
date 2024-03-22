struct MyHashSet {
    hash_set: Vec<i32>,
    size: usize,
    capacity: usize,
}

// Solution #1: More from scratch, doesn't as many built in methods
impl MyHashSet {
    fn new() -> Self {
        return Self {
            hash_set: vec![-1; 2],
            size: 0,
            capacity: 2,
        };
    }

    fn add(&mut self, key: i32) {
        let mut index = self.hash(key);

        loop {
            if self.hash_set[index] == -1 {
                self.hash_set[index] = key;
                break;
            } else {
                if self.hash_set[index] == key {
                    break;
                } else {
                    index = (index + 1) % self.capacity;
                }
            }
        }

        self.size += 1;

        if self.size * 2 >= self.capacity {
            self.rehash();
        }
    }

    fn remove(&mut self, key: i32) {
        let mut index = self.hash(key);
        let mut rehash: bool = false;

        loop {
            if self.hash_set[index] == -1 {
                break;
            } else {
                if self.hash_set[index] == key {
                    self.hash_set[index] = -1;
                    rehash = true;
                    break;
                } else {
                    index = (index + 1) % self.capacity;
                    rehash = true;
                }
            }
        }

        if rehash {
            self.rehash();
        }
    }

    fn contains(&self, key: i32) -> bool {
        let mut index = self.hash(key);

        loop {
            if self.hash_set[index] == -1 {
                return false;
            } else {
                if self.hash_set[index] == key {
                    return true;
                } else {
                    index = (index + 1) % self.capacity;
                }
            }
        }
    }

    fn hash(&self, key: i32) -> usize {
        return key as usize % self.capacity;
    }

    fn rehash(&mut self) {
        let previous_hash_set = self.hash_set.clone();

        let mut new_capacity: usize = self.capacity;

        if self.size * 2 >= self.capacity {
            new_capacity = self.capacity * 2;
        }

        let new_hash_set = vec![-1; new_capacity];
        self.hash_set = new_hash_set;
        self.capacity = new_capacity;
        self.size = 0;

        for value in previous_hash_set.iter() {
            if *value != -1 {
                self.add(*value);
            }
        }
    }

    fn print(&self) {
        for num in self.hash_set.iter() {
            println!("{}", num);
        }
    }
}

fn main() {
    let mut thing = MyHashSet::new();
    thing.add(1);
    thing.add(9);
    thing.add(5);
    thing.remove(4);
    thing.remove(5);
    println!("contains: {:?}", thing.contains(4));
    thing.print();
}

// struct MyHashSet {
//     hash_set: Vec<i32>,
// }
//
// // Solution #2: More simple, Using rust's built in functions
// impl MyHashSet {
//     fn new() -> Self {
//         return Self {
//             hash_set: Vec::new(),
//         };
//     }
//
//     fn add(&mut self, key: i32) {
//         if !self.contains(key) {
//             self.hash_set.push(key);
//         }
//     }
//
//     fn remove(&mut self, key: i32) {
//         if let Some(index) = self.hash_set.iter().position(|&x| x == key) {
//             self.hash_set.remove(index);
//         }
//     }
//
//     fn contains(&self, key: i32) -> bool {
//         return self.hash_set.contains(&key);
//     }
//
//     fn print(&self) {
//         for num in self.hash_set.iter() {
//             println!("{}", num);
//         }
//     }
// }
