int adjacentElementsProduct(int[] inputArray) {
    int sum1 = inputArray[0] * inputArray[1];
    int prod = 0;
    for(int i =0; i<inputArray.length-1;i++){
        prod = inputArray[i]*inputArray[i+1];
        if(sum1<prod){
            sum1 = prod;
        }
    }
    return sum1;
}
