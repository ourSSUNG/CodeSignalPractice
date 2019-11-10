int matrixElementsSum(int[][] matrix) {
    int row = matrix.length;
    int column = matrix[0].length;
    int sum1 = 0;
    for(int i=0;i<row;i++){
        for(int j=0;j<column;j++){
            sum1 = sum1 + matrix[i][j];
            if(matrix[i][j]==0){
                for(int k=i+1;k<row;k++){
                    matrix[k][j] = 0;
                }
            }
        }
    }
    return sum1;
}
