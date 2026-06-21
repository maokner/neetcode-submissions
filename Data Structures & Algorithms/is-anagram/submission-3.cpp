class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> counts(26, 0);
        for (char c : s){
            int idx = c - 'a';
            counts[idx] += 1;
        }

        for (char c : t){
            int idx = c - 'a';
            counts[idx] -= 1;
        }
        for (int i = 0; i < 26; i++){
            if (counts[i] != 0){
                return false;
            }
        }
        return true;
        
    }
};
