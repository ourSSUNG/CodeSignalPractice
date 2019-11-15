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
int kthSmallestInBST(Tree<Integer> t, int k) {
    int[] room = new int[1];
    binarySearch(t,1,k,room);
    return room[0];
}

int binarySearch(Tree<Integer> t,int kth,int key,int[] anslist){
    int num = 0;
    if(t.left!=null&&t.right==null){
        num = binarySearch(t.left,kth,key,anslist);
        if(num==key){
            anslist[0] = t.value;
        }
        return num+1;
    }
    if(t.left==null&&t.right!=null){
        if(kth==key){
            anslist[0] = t.value;
        }
        num = binarySearch(t.right,kth+1,key,anslist);
        return num;
    }
    if(t.left==null&&t.right==null){
        if(kth==key){
            anslist[0] = t.value;
        }
        return kth+1;
    }
    if(t.left!=null&&t.right!=null){
        num = binarySearch(t.left,kth,key,anslist);
        if(num==key){
            anslist[0] = t.value;
        }
        num = binarySearch(t.right,num+1,key,anslist);
        return num;
    }
    return 0;
}
