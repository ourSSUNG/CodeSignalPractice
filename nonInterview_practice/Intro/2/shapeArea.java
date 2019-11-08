int shapeArea(int n) {
    int i = 1;
    int sum = 1;
    while (i < n) {
        sum = sum+ i*4;
        i++;    
    }
    return sum;
}
