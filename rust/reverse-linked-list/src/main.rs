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
    // SOLUTION #3
    // fn do_this(
    //     new: Option<Box<ListNode>>,
    //     previous: Option<Box<ListNode>>,
    // ) -> Option<Box<ListNode>> {
    //     return match new {
    //         Some(node) => do_this(
    //             node.next,
    //             Some(Box::new(ListNode {
    //                 val: node.val,
    //                 next: previous,
    //             })),
    //         ),
    //         None => previous,
    //     };
    // }
    // fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     return do_this(head, None);
    // }
    // SOLUTION #2
    // fn do_this( new: Option<Box<ListNode>>, previous: Option<Box<ListNode>>,) -> Option<Box<ListNode>> {
    // if let Some(node) = new { return do_this(
    //             node.next,
    //             Some(Box::new(ListNode {
    //                 val: node.val,
    //                 next: previous,
    //             })),
    //         );
    //     } else {
    //         return previous;
    //     }
    // }
    // fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     return do_this(head, None);
    // }

    // SOLUTION #1 -- fastest and most memory efficient
    fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut new_list: Option<Box<ListNode>>;
        if let Some(node) = head {
            new_list = Some(Box::new(ListNode::new(node.val)));
            let mut cont: bool = true;
            let mut next_node: ListNode;
            next_node = *node;

            while cont {
                if let Some(node) = next_node.next {
                    new_list = Some(Box::new(ListNode {
                        val: node.val,
                        next: new_list,
                    }));
                    next_node = *node;
                } else {
                    cont = false;
                }
            }
            return new_list;
        } else {
            return None;
        }
    }

    let head = Some(Box::new(ListNode {
        val: 5,
        next: Some(Box::new(ListNode {
            val: 4,
            next: Some(Box::new(ListNode {
                val: 3,
                next: Some(Box::new(ListNode {
                    val: 2,
                    next: Some(Box::new(ListNode::new(1))),
                })),
            })),
        })),
    }));

    let answer = reverse_list(head.clone());

    fn print_answer(head: Option<Box<ListNode>>) {
        if let Some(node) = head {
            println!("{}", node.val);
            print_answer(node.next)
        }
    }

    print_answer(answer);
}
