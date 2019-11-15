String findProfession(int level, int pos) {
    int levpoint = 1;
    for(int i = 1; i<level-1;i++){
        levpoint = levpoint*2;
    }
    pos = pos -1;
    int checker = 0;
    while(levpoint!=0){
        checker = checker + pos/levpoint;
        
        pos = pos%levpoint;
        levpoint = levpoint/2;
    }
    if (checker%2 == 0){
        return "Engineer";
    }
    else{
        return "Doctor";
    }
}
