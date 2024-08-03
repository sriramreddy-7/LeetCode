class Solution {
    public int countKDifference(int[] nums, int k) {
        int i,j,c=0;
        for(i=0;i<nums.length;i++)
        {
            for(j=i+1;j<nums.length;j++)
            {
                if( nums[i]-nums[j]==k || nums[j]-nums[i]==k)
                {
                    c=c+1;
                }
            }
        }
        return c;
    }
}