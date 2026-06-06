class Solution {

    public int removeDuplicates(int[] nums) {

        if(nums.length <= 2) {
            return nums.length;
        }

        int k = 2;

        for(int i = 2; i < nums.length; i++) {

            if(nums[i] != nums[k - 2]) {

                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }

    public static void main(String[] args) {

        Solution obj = new Solution();

        int[] nums = {1,1,1,2,2,3};

        int k = obj.removeDuplicates(nums);

        System.out.println("k = " + k);

        for(int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}