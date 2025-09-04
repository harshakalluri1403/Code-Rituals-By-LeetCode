class Solution {
public:
    int findClosest(int x, int y, int z) {
        int first = ((z-x)<0) ? -(z-x) : z-x;
        int second = ((z-y)<0) ? -(z-y) : z-y;
        // cout << first << second;
        // return 0;
        if (first < second){
            return 1;
        }else if(second < first){
            return 2;
        }else{
            return 0;
        }
        
    }
};