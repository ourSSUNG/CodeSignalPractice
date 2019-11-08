int makeArrayConsecutive2(int[] statues) {
    int max1 = statues[0];
    int min1 = statues[0];
    for(int i=1;i<statues.length;i++){
        if(max1<statues[i]){
            max1 = statues[i];
        }
        if(min1>statues[i]){
            min1 = statues[i];
        }
    }
    return (max1 - min1 + 1) - statues.length;
}
