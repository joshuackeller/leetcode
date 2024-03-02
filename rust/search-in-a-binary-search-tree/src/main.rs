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

fn search_bst(mut root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
    while let Some(r) = root {
        let rb = r.borrow();
        if rb.val < val {
            root = rb.right.clone();
        } else if rb.val > val {
            root = rb.left.clone();
        } else {
            return Some(r.clone());
        }
    }

    return None;
}

fn main() {
    let mut root = None;
    for i in 1..=10 {
        root = insert(root, i);
    }

    let result = search_bst(root, 5);

    if let Some(r) = result {
        println!("{}", r.borrow().val)
    } else {
        println!("not found")
    }
}
