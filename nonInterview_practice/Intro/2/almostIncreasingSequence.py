boolean almostIncreasingSequence(int[] sequence) {
    int stack = 0;
    int tmp = 0;
    Vector<Integer> seq = new Vector<Integer>(sequence.length,1);
    seq.add(0,sequence[0]);
    for(int i =1;i<sequence.length;i++){
        seq.add(i,sequence[i]);
        if (sequence[i]<=sequence[i-1]){
            tmp = i;
        }
    }
    int tmp2 = seq.elementAt(tmp-1);
    seq.remove(tmp-1);
    
    
    for(int i = 1; i<seq.size();i++){
        if (seq.elementAt(i)<=seq.elementAt(i-1)){
            stack++;
            break;
        }
    }
    if(stack ==0 ){
        return true;
    }
    seq.add(tmp-1,tmp2);
    seq.remove(tmp);
    
    for(int i = 1; i<seq.size();i++){
        if (seq.elementAt(i)<=seq.elementAt(i-1)){
            stack++;
            break;
        }
    }
    if (stack>1){
        return false;
    }
    else{
        return true;
    }
}
