class Solution {
    public int countDigits(int num) {
        String num_str=Integer.toString(num);
        int flag,count=0;
        for(char c:num_str.toCharArray())
        {
            flag=Character.getNumericValue(c);
            if(flag!=0 && num%flag==0)
            {
                count+=1;
            } 
        }
        return count;
    }
}