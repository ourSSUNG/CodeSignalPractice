boolean isLucky(int n) {
    int k = n;
    int rog = 0;
    while(k>=10){
        k = k/10;
        rog++;
    }
    rog++;
    rog = rog/2;
    k = n;
    int lsum = 0;
    for(int i =0;i<rog;i++){
        lsum= lsum + k%10;
        k = k/10;
    }
    int rsum = 0;
    for(int i =0;i<rog;i++){
        rsum= rsum + k%10;
        k = k/10;
    }
    return rsum==lsum;
}
