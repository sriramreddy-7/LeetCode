class Solution {
    public void reverseString(char[] s) {
        int i=0,j=(s.length)-1;
        char t;
        while (i<=j)
        {
            // t="";
            t=s[i];
            s[i]=s[j];
            s[j]=t;
            i=i+1;
            j=j-1;
        }
    }
}