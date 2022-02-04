public class AvlTree extends BinarySearchTree{
    private static final int ALLOWED_IMBALANCE = 1;

    public AvlTree(int[] array) {
        super(array);
        root = balance((AvlNode) root);
    }

    private AvlNode balance(AvlNode root) {
        //Case 1: single rotation at k2 (root) with k1 (k2's left child)
        //Case 2: double rotation at k3 (root) with k1 (k3's left child) and k2(k1's right child)
        if(height(root.left) - height(root.right) > ALLOWED_IMBALANCE){
            if(height(root.left.left) >= height(root.left.right)){ //case 1
                root = singleRotationWithLeftChild(root);
            }else{ //case 2
                root = doubleRotationWithLeftChild(root);
            }
        }
        //Case 3: double rotation at k1 (root) with k3 (k1's right child) and k2(k3's left child)
        //Case 4 single rotation at k1 (root) with k2 (k1's right child)
        else if(height(root.right) - height(root.left) > ALLOWED_IMBALANCE){
            if(height(root.right.right) >= height(root.right.left)){ //case 4
                root = singleRotationWithRightChild(root);
            }else{ //case 3
                root = doubleRotationWithRightChild(root);
            }
        }
        root.depth = findDepth(root);
        return root;
    }

    //Case 1: single rotation at k2 (root) with k1 (k2's left child)
    private AvlNode singleRotationWithLeftChild(AvlNode k2) {
        AvlNode k1 = (AvlNode)k2.left;
        k2.left = k1.right;
        k1.right = k2;
        k2.depth = findDepth(k2);
        k1.depth = findDepth(k1);
        return k1;
    }

    //Case 4 single rotation at k1 (root) with k2 (k1's right child)
    private AvlNode singleRotationWithRightChild(AvlNode k1){
        AvlNode k2 = (AvlNode) k1.right;
        k1.right = k2.left;
        k2.left = k1;
        k1.depth = findDepth(k1);
        k2.depth = findDepth(k2);
        return k2;
    }

    //Case 2: double rotation at k3 (root) with k1 (k3's left child) and k2(k1's right child)
    private AvlNode doubleRotationWithLeftChild(AvlNode k3) {
        k3.left = singleRotationWithRightChild((AvlNode) k3.left);
        return singleRotationWithLeftChild(k3);
    }

    //Case 3: double rotation at k1 (root) with k3 (k1's right child) and k2(k3's left child)
    private AvlNode doubleRotationWithRightChild(AvlNode k1) {
        k1.right = singleRotationWithLeftChild((AvlNode) k1.right);
        return singleRotationWithRightChild(k1);
    }


    private int height(BinaryNode root) {
        return root == null ? -1 : findDepth(root);
    }

    private int findDepth(BinaryNode root) {
        return Math.max(height(root.left), height(root.right)) + 1;
    }

    public static class AvlNode extends BinarySearchTree.BinaryNode {
        public int depth;

        public AvlNode(int data, BinarySearchTree.BinaryNode left, BinarySearchTree.BinaryNode right, int depth) {
            super(data, left, right);
            this.depth = depth;
        }

        public AvlNode(int data, BinarySearchTree.BinaryNode left, BinarySearchTree.BinaryNode right) {
            this(data, left, right, 0);
        }

        public AvlNode(int data) {
            this(data, null, null, 0);
        }
    }
}
