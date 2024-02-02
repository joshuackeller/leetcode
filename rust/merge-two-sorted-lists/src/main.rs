// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

fn main() {
    fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut nums: Vec<i32> = vec![];

        let mut list1_copy = list1.clone();
        while let Some(node) = list1_copy {
            nums.push(node.val);
            list1_copy = node.next;
        }

        let mut list2_copy = list2;
        while let Some(node) = list2_copy {
            nums.push(node.val);
            list2_copy = node.next;
        }

        nums.sort();

        for num in nums.iter() {
            println!("{}", num);
        }

        return list1;
    }

    // TEST INFO
    let list1 = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 2,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));
    let list2 = Some(Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 3,
            next: Some(Box::new(ListNode { val: 4, next: None })),
        })),
    }));

    let mut answer: Option<Box<ListNode>> = merge_two_lists(list1, list2);

    // while let Some(node) = answer {
    //     println!("{}", node.val);
    //     answer = node.next;
    // }
}
