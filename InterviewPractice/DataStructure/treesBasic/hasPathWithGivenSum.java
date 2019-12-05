//
// Binary trees are already defined with this interface:
// class Tree<T> {
//   Tree(T x) {
//     value = x;
//   }
//   T value;
//   Tree<T> left;
//   Tree<T> right;
// }
boolean hasPathWithGivenSum(Tree<Integer> t, int s) {
    if(t==null){
        return false;
    }
    boolean flag = treeChecker(t,0,s);
    return flag;
}

boolean treeChecker(Tree<Integer> t, int sum,int goal){
    if(t.left==null&&t.right==null){
        if(sum+t.value == goal){
            return true;
        }
        else{
            return false;
        }
    }
    boolean rb;
    boolean lb;
    if(t.left!=null){
        lb = treeChecker(t.left,sum+t.value,goal);
        if(lb == true){
            return lb;
        }
    }
    if(t.right!=null){
        rb = treeChecker(t.right,sum+t.value,goal);
        return rb;
    }
    return false;
}
