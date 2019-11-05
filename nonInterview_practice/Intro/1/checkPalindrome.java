boolean checkPalindrome(String inputString) {
    boolean b = true;
    int len = inputString.length();
    for ( int i = 0; i < len/2; i++){
        if(inputString.charAt(i)!=inputString.charAt(len-i-1)){
            b = false;
        }
    }
    return b;
                                      
                                      
}
