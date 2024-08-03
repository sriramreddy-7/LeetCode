import java.util.*;
class Solution {
    public int[] getConcatenation(int[] nums) {
     int i,j,c=0;
     int[] temp = new int[2*(nums.length)];
     for(i=0;i<2;i++)
     {
        for(j=0;j<nums.length;j++)
        {
            temp[c]=nums[j];
            c=c+1;
        }
     }
     return temp;
    }
}