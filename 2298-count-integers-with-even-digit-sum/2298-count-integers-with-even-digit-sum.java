class Solution {
    public int countEven(int num) {
    int r=0,s=0,count=0,temp;
    for(int i=1;i<=num;i++)
    {
        temp=i;
        while(temp!=0)
        {
            r=temp%10;
            s=s+r;
            temp=temp/10;
        }
        if (s%2==0)
        {
            count+=1;
        }
        s=0;
        r=0;
    }
    return count;
    }
}