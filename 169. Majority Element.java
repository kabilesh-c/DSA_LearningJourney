class Solution {

    public int majorityElement(int[] nums) {

        int candidate = 0;
        int count = 0;

        for(int num : nums) {

            if(count == 0) {
                candidate = num;
            }

            if(num == candidate) {
                count++;
            }
            else {
                count--;
            }
        }

        return candidate;
    }

    public static void main(String[] args) {

        Solution obj = new Solution();

        int[] nums = {2,2,1,1,1,2,2};

        System.out.println(obj.majorityElement(nums));
    }
}