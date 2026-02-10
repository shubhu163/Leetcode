class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), 
     [](const vector<int>& a, const vector<int>& b) {
         return a[1] < b[1];  // Sort by END time
     });
        int count = 0;
        int end = INT_MIN;

        for (auto& interval : intervals){
            int start = interval[0];
            int end1 = interval[1];

            if (start >= end) end = end1;
            else count++;


        }
        return count;


        
    }
};

