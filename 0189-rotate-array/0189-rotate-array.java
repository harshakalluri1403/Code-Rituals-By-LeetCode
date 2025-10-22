class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length; 
        
        ArrayList<Integer> newArray = new ArrayList<>();
        
        for (int i = nums.length - k; i < nums.length; i++) {
            newArray.add(nums[i]);
        }
        
        for (int i = 0; i < nums.length - k; i++) {
            newArray.add(nums[i]);
        }
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = newArray.get(i);
        }

        System.out.println(Arrays.toString(nums));
    }
}
