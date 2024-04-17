// Definition for a binary tree node.
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

use std::cell::RefCell;
use std::rc::Rc;

pub struct Solution;

impl Solution {
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        return "blach".to_string();
    }
}

fn main() {
    let root = Rc::new(RefCell::new(TreeNode::new(25)));
    root.borrow_mut().left = Some(Rc::new(RefCell::new(TreeNode::new(1))));
    root.borrow_mut().right = Some(Rc::new(RefCell::new(TreeNode::new(3))));
    root.borrow().left.as_ref().unwrap().borrow_mut().left =
        Some(Rc::new(RefCell::new(TreeNode::new(1))));
    root.borrow().left.as_ref().unwrap().borrow_mut().right =
        Some(Rc::new(RefCell::new(TreeNode::new(3))));
    root.borrow().right.as_ref().unwrap().borrow_mut().left =
        Some(Rc::new(RefCell::new(TreeNode::new(0))));
    root.borrow().right.as_ref().unwrap().borrow_mut().right =
        Some(Rc::new(RefCell::new(TreeNode::new(2))));

    let result = Solution::smallest_from_leaf(Some(root));

    println!("{}", result);
}
