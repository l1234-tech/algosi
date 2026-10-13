#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

pair<vector<int>, long long> merge_and_count(const vector<int>& arr) {
    if (arr.size() <= 1) {
        return {arr, 0};
    }
    
    int mid = arr.size() / 2;
    vector<int> left_arr(arr.begin(), arr.begin() + mid);
    vector<int> right_arr(arr.begin() + mid, arr.end());
    
    auto [left, left_inv] = merge_and_count(left_arr);
    auto [right, right_inv] = merge_and_count(right_arr);
    
    vector<int> merged;
    merged.reserve(arr.size());
    
    long long inv_count = left_inv + right_inv;
    size_t i = 0, j = 0;
    
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            merged.push_back(left[i]);
            i++;
        } else {
            merged.push_back(right[j]);
            inv_count += left.size() - i;
            j++;
        }
    }
    
    while (i < left.size()) {
        merged.push_back(left[i]);
        i++;
    }
    while (j < right.size()) {
        merged.push_back(right[j]);
        j++;
    }
    
    return {merged, inv_count};
}

int main() {
    ifstream f("input.txt");
    
    int n;
    f >> n;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        f >> a[i];
    }
    
    auto [sorted, total] = merge_and_count(a);
    cout << total << endl;
    
    return 0;
}