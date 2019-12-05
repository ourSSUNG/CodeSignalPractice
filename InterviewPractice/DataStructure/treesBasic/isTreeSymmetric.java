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
boolean isTreeSymmetric(Tree<Integer> t) {
    if (t==null){
        return true;
    }
    if(t.left!=null&&t.right==null){
        return false;
    }
    if(t.left==null&&t.right!=null){
        return false;
    }
    if(t.left==null&&t.right==null){
        return true;
    }
    
    return treeCompare(t.left,t.right);
}

boolean treeCompare(Tree<Integer> lt, Tree<Integer> rt){
    int asdf = (lt.value-rt.value);
    
    if(asdf!=0){
        return false;
    }
    if(lt.right==null&&lt.left==null){
        if(rt.right==null&&rt.left==null){
            return true;
        }
        else{
            
            return false;
        }
    }
    if(lt.right==null&&lt.left!=null){
        if(rt.right!=null&&rt.left==null){
            return treeCompare(lt.left,rt.right);
        }
        else{
            return false;
        }
    }
    if(lt.right!=null&&lt.left==null){
        if(rt.right==null&&rt.left!=null){
            return treeCompare(lt.right,rt.left);
        }
        else{
            return false;
        }
    }
    if(rt.right!=null&&rt.left!=null){
        
        return (treeCompare(lt.right,rt.left)&&treeCompare(lt.left,rt.right));
    }
    else{
        return false;
    }
}
