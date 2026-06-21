class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            int need = target - num;
            if (hashmap.contains(need)){
                return {hashmap.at(need), i};
            }
            else{
                hashmap[num] = i;
            }
        }
        
    }
};
