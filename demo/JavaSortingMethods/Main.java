import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String method = args[0];
        String a = args[1];
        int[] array = convertStringToArray(a);

        if (method.equals("HeapSort")) {
            HeapSort heapSort = new HeapSort(array);
            array = heapSort.sort();
            System.out.println(Arrays.toString(array));
        }
        if (method.equals("QuickSort")) {
            QuickSort.quickSort(array, 0, array.length);
        }
        if (method.equals("BinarySearchTree")) {
            BinarySearchTree binarySearchTree = new BinarySearchTree(array);
            binarySearchTree.readTree();
        }
        if (method.equals("AvlTree")) {
            AvlTree avlTree = new AvlTree(array);
            avlTree.readTree();
        }
    }

    private static int[] convertStringToArray(String s) {
        String[] stringList = s.split(", ");
        int[] integerList = new int[stringList.length];
        for (int i = 0; i < stringList.length; i++) {
            integerList[i] = Integer.parseInt(stringList[i]);
        }
        return integerList;
    }
}
