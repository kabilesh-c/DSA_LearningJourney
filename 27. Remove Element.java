class Solution {

    public int removeElement(int[] nums, int val) {

        int k = 0;

        for(int i = 0; i < nums.length; i++) {

            if(nums[i] != val) {

                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }

    public static void main(String[] args) {

        Solution obj = new Solution();

        int[] nums = {3,2,2,3};

        int k = obj.removeElement(nums, 3);

        System.out.println("k = " + k);

        for(int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}