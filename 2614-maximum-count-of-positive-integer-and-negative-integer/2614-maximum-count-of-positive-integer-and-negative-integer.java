class Solution {
    public int maximumCount(int[] nums) {
        int p=0,n=0;
        for (int num:nums)
        {
            if(num>0)
            {
                p=p+1;
            }
            else
            { 
                if(num<0)
                {
                    n=n+1;
                }
            }
        }
        if(p>n)
        {
            return p;
        }
        else
        {
            return n;
        }
    }
}