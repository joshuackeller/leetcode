#include <iostream>

using namespace std;

//  g++ -std=c++11 main.cpp && ./a.out

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  // SOLUTION #2 - TWO POINTERS
  ListNode *reverseList(ListNode *head) {

    ListNode *prev = NULL;
    ListNode *curr = head;

    while (curr != NULL) {
      ListNode *nextPointer = curr->next;
      curr->next = prev;
      prev = curr;
      curr = nextPointer;
    }

    return prev;
  }
  // SOLUTION #1 - NEW LIST
  // ListNode *reverseList(ListNode *head) {
  //   if (head != NULL) {
  //     ListNode *newList = new ListNode(head->val);

  //    head = head->next;

  //    while (head != NULL) {
  //      newList = new ListNode(head->val, newList);
  //      head = head->next;
  //    }

  //    return newList;

  //  } else {
  //    return head;
  //  }
  //}
};

int main() {
  ListNode *head = new ListNode(5);
  head->next = new ListNode(4);
  head->next->next = new ListNode(3);
  head->next->next->next = new ListNode(2);
  head->next->next->next->next = new ListNode(1);

  Solution solution;
  ListNode *answer = solution.reverseList(head);

  while (answer != NULL) {
    cout << answer->val;
    answer = answer->next;
  }

  return 0;
}

// while(curr != NULL){
//             ListNode* forward = curr->next; // forward = val: 3; next: 2
//             curr->next = prev; // curr->next = val: 5; next: NULL
//             prev = curr; // prev = val: 4; next: 3;
//             curr = forward; // curr = val: 4; next: 3
//
// }
