use std::cell::RefCell;
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

pub struct Solution;

impl Solution {
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
        return Solution::test_tree(root, target_sum, 0);
    }
    pub fn test_tree(
        root: Option<Rc<RefCell<TreeNode>>>,
        target_sum: i32,
        running_sum: i32,
    ) -> bool {
        if let Some(r) = root {
            let rb = r.borrow();
            let new_sum: i32 = rb.val + running_sum;

            if rb.left.is_some()
                && Solution::test_tree(rb.left.clone(), target_sum, new_sum) == true
            {
                return true;
            }
            if rb.right.is_some()
                && Solution::test_tree(rb.right.clone(), target_sum, new_sum) == true
            {
                return true;
            }
            if target_sum == new_sum {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
}

fn main() {
    // Create the tree nodes
    let node_5 = Rc::new(RefCell::new(TreeNode::new(5)));
    let node_4 = Rc::new(RefCell::new(TreeNode::new(4)));
    let node_8 = Rc::new(RefCell::new(TreeNode::new(8)));
    let node_11 = Rc::new(RefCell::new(TreeNode::new(11)));
    let node_13 = Rc::new(RefCell::new(TreeNode::new(13)));
    let node_4_2 = Rc::new(RefCell::new(TreeNode::new(4)));
    let node_7 = Rc::new(RefCell::new(TreeNode::new(7)));
    let node_2 = Rc::new(RefCell::new(TreeNode::new(2)));
    let node_1 = Rc::new(RefCell::new(TreeNode::new(1)));

    // Build the tree structure
    node_5.borrow_mut().left = Some(node_4.clone());
    node_5.borrow_mut().right = Some(node_8.clone());
    node_4.borrow_mut().left = Some(node_11.clone());
    node_11.borrow_mut().left = Some(node_7.clone());
    node_11.borrow_mut().right = Some(node_2.clone());
    node_8.borrow_mut().left = Some(node_13.clone());
    node_8.borrow_mut().right = Some(node_4_2.clone());
    node_4_2.borrow_mut().right = Some(node_1.clone());

    let answer = Solution::has_path_sum(Some(node_5), 22);

    println!("{}", answer);
}
