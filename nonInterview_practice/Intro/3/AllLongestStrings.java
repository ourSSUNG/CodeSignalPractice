String[] allLongestStrings(String[] inputArray) {
    int maxlen = 0;
    for(int i =0 ; i< inputArray.length;i++){
        if(maxlen<inputArray[i].length()){
            maxlen = inputArray[i].length();
        }
    }
    ArrayList<String> ans = new ArrayList<String>();
        
    for(int i =0 ; i< inputArray.length;i++){
        if(maxlen==inputArray[i].length()){
            
            ans.add(inputArray[i]);
        }
    }
    String[] ans2 = new String[ans.size()];
    for(int i = 0; i<ans2.length;i++){
        ans2[i] = ans.get(i);
    }
    
    return ans2;
}
