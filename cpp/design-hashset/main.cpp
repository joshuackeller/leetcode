#include <iostream>

using namespace std;

//  g++ -std=c++11 main.cpp && ./a.out

// SOLUTION #2: Simple, relies on built in c++ methods
class MyHashSet {
private:
  vector<int> hashSet;

public:
  void add(int key) {
    if (!contains(key)) {
      hashSet.push_back(key);
    }
  }

  void remove(int key) {
    auto k = find(hashSet.begin(), hashSet.end(), key);
    if (k != hashSet.end()) {
      hashSet.erase(k);
    }
  }

  bool contains(int key) {
    return (find(hashSet.begin(), hashSet.end(), key) != hashSet.end());
  }
};

int main() {
  MyHashSet *obj = new MyHashSet();
  obj->add(1);
  obj->add(9);
  obj->add(17);
  obj->remove(9);
  cout << obj->contains(17);
}

// SOLUTION #1: comples, from scratch solutio
// class MyHashSet {
// private:
//   int *array;
//   int size = 0;
//   int capacity = 2;
//
//   int hash(int key) { return key % capacity; }
//   void rehash() {
//     int *previousArray = array;
//     int previousCapacity = capacity;
//
//     if ((capacity / 2) <= size) {
//       capacity = capacity * 2;
//     }
//     size = 0;
//     array = new int[capacity];
//     for (int x = 0; x < capacity; x++) {
//       array[x] = -1;
//     }
//
//     for (int x = 0; x < previousCapacity; x++) {
//       if (previousArray[x] != -1) {
//         add(previousArray[x]);
//       }
//     }
//   }
//
// public:
//   MyHashSet() {
//     array = new int[capacity];
//     for (int x = 0; x < capacity; x++) {
//       array[x] = -1;
//     }
//   }
//
//   void add(int key) {
//     int index = hash(key);
//
//     while (true) {
//       if (array[index] == -1) {
//         array[index] = key;
//         break;
//       } else {
//         if (array[index] == key) {
//           break;
//         } else {
//           index = (index + 1) % capacity;
//         }
//       }
//     }
//
//     size += 1;
//
//     if ((size * 2) >= capacity) {
//       rehash();
//     }
//   }
//
//   void remove(int key) {
//     int index = hash(key);
//
//     while (true) {
//       if (array[index] == -1) {
//         break;
//       } else {
//         if (array[index] == key) {
//           array[index] = -1;
//           break;
//         } else {
//           index = (index + 1) % capacity;
//         }
//       }
//     }
//
//     size -= 1;
//
//     rehash();
//   }
//
//   bool contains(int key) {
//     int index = hash(key);
//     while (true) {
//       if (array[index] == -1) {
//         return false;
//       } else {
//         if (array[index] == key) {
//           return true;
//         } else {
//           index = (index + 1) % capacity;
//         }
//       }
//     }
//     return true;
//   }
//
//   void print() {
//     for (int x = 0; x < capacity; x++) {
//       cout << array[x] << ", ";
//     }
//   }
// };
