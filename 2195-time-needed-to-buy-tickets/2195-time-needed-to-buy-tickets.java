class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int i=0,time=0;
		while(tickets[k]!=0)
		 {
				 if(tickets[i]!=0)
				 {
					 tickets[i]-=1;
					 time+=1;
				 }
				 i++;
				 if(i>=tickets.length)
				 {
					 i=0;
				 }
		 }
		 return time;
    }
}