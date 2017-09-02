class Solution {
public:
    int reverse(int x) {
        long sum = 0;
        while(x!=0){
            sum = sum*10 + x%10;
            x /= 10;}
        return (sum<INT_MIN || sum>INT_MAX)? 0 : int(sum);
    }
};
