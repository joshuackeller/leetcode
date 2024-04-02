
#include <chrono>
#include <cinttypes>
#include <iostream>
#include <queue>
#include <sstream>
#include <unordered_set>
#include <vector>

using namespace std;
using namespace std::chrono;

// g++ -std=c++11 main.cpp && ./a.out

// SOLUTION #2: BFS
class Solution {
public:
  int shortestPathBinaryMatrix(vector<vector<int>> &grid) {
    int R_MAX = grid.size() - 1;
    int C_MAX = grid[0].size() - 1;

    if (grid[0][0] == 1 || grid[R_MAX][C_MAX] == 1) {
      return -1;
    }

    vector<vector<int>> nextOptions = {{-1, 0}, {-1, -1}, {-1, 1}, {1, 0},
                                       {1, -1}, {1, 1},   {0, -1}, {0, 1}};

    unordered_set<string> visited;
    queue<tuple<int, int>> gridQueue;

    visited.insert("0:0");
    gridQueue.push(make_tuple(0, 0));

    int size = 0;
    while (!gridQueue.empty()) {
      size++;
      int queueSize = gridQueue.size();
      for (int x = 0; x < queueSize; x++) {
        tuple<int, int> pair = gridQueue.front();
        gridQueue.pop();
        int r = get<0>(pair);
        int c = get<1>(pair);

        if (r == R_MAX && c == C_MAX) {
          return size;
        }

        for (int y = 0; y < nextOptions.size(); y++) {
          int nr = r + nextOptions[y][0];
          int nc = c + nextOptions[y][1];

          stringstream ss;
          ss << nr << ":" << nc;
          string set = ss.str();
          bool hasVisited = visited.find(set) != visited.end();

          if (!hasVisited && nr >= 0 && nc >= 0 && nr <= R_MAX && nc <= C_MAX &&
              grid[nr][nc] != 1) {
            gridQueue.push(make_tuple(nr, nc));
            visited.insert(set);
          }
        }
      }
    }
    return -1;
  }
};

int main() {
  Solution solution;

  vector<vector<int>> grid = {{0, 0, 0, 0, 1},
                              {1, 0, 0, 0, 0},
                              {0, 1, 0, 1, 0},
                              {0, 0, 0, 1, 1},
                              {0, 0, 0, 1, 0}};
  //   vector<vector<int>> grid = {{0, 0, 0}, {1, 1, 0}, {1, 1, 0}};

  auto start = high_resolution_clock::now();

  int result = solution.shortestPathBinaryMatrix(grid);

  cout << "\n" << result << "\n";

  auto duration =
      duration_cast<milliseconds>(high_resolution_clock::now() - start);

  cout << duration.count() << " milliseconds" << endl;

  return 0;
}

// SOLUTION #1: DFS Times out becuase time complexity is 8^(n*m)
// class Solution {
// public:
//   int shortestPathBinaryMatrix(vector<vector<int>> &grid) {
//     unordered_set<string> visited;
//
//     int height = grid.size() - 1;
//     int width = grid[0].size() - 1;
//
//     if (grid[0][0] == 1 || grid[height][width] == 1) {
//       return -1;
//     }
//
//     return searchPath(grid, 0, 0, 0, visited);
//   }
//   int searchPath(vector<vector<int>> &grid, int r, int c, int count,
//                  unordered_set<string> visited) {
//     // Check if value has already been visited
//     stringstream ss;
//     ss << r << ":" << c;
//     string set = ss.str();
//     if (visited.find(set) == visited.end()) {
//       visited.insert(set);
//     } else {
//       return -1;
//     }
//
//     // Check if value is out of bounds
//     int height = grid.size() - 1;
//     int width = grid[0].size() - 1;
//
//     if (r > height || c > width || r < 0 || c < 0) {
//       return -1;
//     }
//
//     count++;
//     // Check if value is 1 or 0
//     if (grid[r][c] == 1) {
//       return -1;
//     } else {
//       // Check if is end and path exists
//       if (r == height && c == width) {
//         return count;
//       } else {
//         vector<int> results;
//
//         results.push_back(searchPath(grid, r, c + 1, count, visited));
//         results.push_back(searchPath(grid, r, c - 1, count, visited));
//         results.push_back(searchPath(grid, r + 1, c, count, visited));
//         results.push_back(searchPath(grid, r + 1, c + 1, count, visited));
//         results.push_back(searchPath(grid, r + 1, c - 1, count, visited));
//         results.push_back(searchPath(grid, r - 1, c, count, visited));
//         results.push_back(searchPath(grid, r - 1, c + 1, count, visited));
//         results.push_back(searchPath(grid, r - 1, c - 1, count, visited));
//
//         bool pathExists = false;
//         int lowestCount = -1;
//         for (int x = 0; x < results.size(); x++) {
//           if (results[x] != -1) {
//             pathExists = true;
//             if (lowestCount == -1) {
//               lowestCount = results[x];
//             } else {
//               lowestCount = min(lowestCount, results[x]);
//             }
//           }
//         }
//
//         if (!pathExists) {
//           return -1;
//         } else {
//           return lowestCount;
//         }
//       }
//     }
//   }
// };
