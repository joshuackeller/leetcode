use core::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut order: Vec<i32> = Vec::new();

    if let Some(r) = root {
        let rb = r.borrow();

        let left: Vec<i32> = inorder_traversal(rb.left.clone());
        order.extend(left);

        order.push(rb.val);

        let right: Vec<i32> = inorder_traversal(rb.right.clone());
        order.extend(right);
    }
    return order;
}

fn main() {
    let mut root = None;
    for i in 1..=10 {
        root = insert(root, i);
    }

    let result = inorder_traversal(root);

    for num in result.iter() {
        println!("{}", num);
    }
}

fn insert(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
    match root {
        Some(node) => {
            if val < node.borrow().val {
                let left = insert(node.borrow().left.clone(), val);
                node.borrow_mut().left = left;
            } else if val > node.borrow().val {
                let right = insert(node.borrow().right.clone(), val);
                node.borrow_mut().right = right;
            }
            Some(node)
        }
        None => {
            let new_node = Rc::new(RefCell::new(TreeNode::new(val)));
            Some(new_node)
        }
    }
}
