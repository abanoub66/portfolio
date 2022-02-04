public class BinarySearchTree {

    protected BinaryNode root;

    public BinarySearchTree(int[] array) {
        root = new BinaryNode(array[0]);
        for (int i = 1; i < array.length; i++) {
            add(root, array[i]);
        }
    }

    private void add(BinaryNode current, int data) {
        if (data < current.data) {
            if (current.left == null) {
                current.left = new BinaryNode(data);
            } else {
                add(current.left, data);
            }
        } else {
            if (current.right == null) {
                current.right = new BinaryNode(data);
            } else {
                add(current.right, data);
            }
        }
    }

    public void readTree() {
        readTree(root);
    }

    private void readTree(BinaryNode current) {
        if (current.left != null) {
            readTree(current.left);
        }
        System.out.print(current.data + ", ");
        if (current.right != null) {
            readTree(current.right);
        }
    }

    public static class BinaryNode {
        public int data;
        public BinaryNode left;
        public BinaryNode right;

        public BinaryNode(int data, BinaryNode left, BinaryNode right) {
            this.data = data;
            this.left = left;
            this.right = right;
        }

        public BinaryNode(int data) {
            this(data, null, null);
        }
    }
}