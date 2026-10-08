#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream fin("input.txt");
    if (!fin) { cerr << "no file\n"; return 1; }

    vector<int> prices;
    string line;
    getline(fin, line);
    {
        istringstream iss(line);
        int x;
        while (iss >> x) prices.push_back(x);
    }

    int n = prices.size();
    vector<int> spans(n, 0);
    vector<int> st;
    st.reserve(n);

    for (int i = 0; i < n; ++i) {
        while (!st.empty() && prices[st.back()] <= prices[i]) {
            st.pop_back();
        }
        spans[i] = st.empty() ? i + 1 : i - st.back();
        st.push_back(i);
    }

    for (int i = 0; i < n; ++i) {
        cout << spans[i] << (i + 1 == n ? '\n' : ' ');
    }
    return 0;
}