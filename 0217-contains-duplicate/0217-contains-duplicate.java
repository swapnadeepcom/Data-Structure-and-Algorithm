import java.util.HashSet;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int arr:nums) {
            if (seen.contains(arr)) {
                return true;
            }
            seen.add(arr);
        }
        return false;
    }
}