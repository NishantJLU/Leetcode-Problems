class Solution {
public:
    vector<vector<int>> ans;
    vector<int> path;

    void solve(int start, int target, vector<int>& candidates) {
        if (target == 0) {
            ans.push_back(path);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {

            // Skip duplicates at the same recursion level
            if (i > start && candidates[i] == candidates[i - 1])
                continue;

            // Since array is sorted, no need to continue
            if (candidates[i] > target)
                break;

            path.push_back(candidates[i]);

            // Move to next index (cannot reuse same element)
            solve(i + 1, target - candidates[i], candidates);

            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

        sort(candidates.begin(), candidates.end());

        solve(0, target, candidates);

        return ans;
    }
};