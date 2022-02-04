public class HeapSort {
    private final int[] heap;
    private int size;

    public HeapSort(int[] a) {
        heap = new int[a.length];
        size = 0;
        heapify(a);
    }

    private void heapify(int[] a) {
        for (int i : a) {
            add(i);
        }
    }

    public int[] sort() {
        int[] sorted = new int[size];
        for (int i = 0; i < sorted.length; i++) {
            sorted[i] = next();
        }
        return sorted;
    }

    private void add(int data) {
        heap[size++] = data;
        percolateUp(size - 1);
    }

    private int next() {
        if (!(size > 0)) {
            throw new IndexOutOfBoundsException();
        }
        int min = heap[0];
        heap[0] = heap[--size];
        percolateDown(0);
        return min;
    }

    private void percolateUp(int hole) {
        int parent = (hole - 1) / 4;
        while (hole > 0 && heap[hole] < heap[parent]) {
            int temp = heap[hole];
            heap[hole] = heap[parent];
            heap[parent] = temp;
            hole = parent;
            parent = (hole - 1) / 4;
        }
    }

    private void percolateDown(int hole) {
        int one = 4 * hole + 1;
        int two = one + 1;
        int three = one + 2;
        int four = one + 3;
        while (percolateDownCondition(hole, one, two, three, four)) {
            int min = findMin(one, two, three, four);
            int temp = heap[hole];
            heap[hole] = heap[min];
            heap[min] = temp;
            hole = min;
            one = 4 * hole + 1;
            two = one + 1;
            three = one + 2;
            four = one + 3;
        }
    }

    private int findMin(int one, int two, int three, int four) {
        int min = one;
        if (two < size && heap[two] < heap[min]) {
            min = two;
        }
        if (three < size && heap[three] < heap[min]) {
            min = three;
        }
        if (four < size && heap[four] < heap[min]) {
            min = four;
        }
        return min;
    }

    private boolean percolateDownCondition(int hole, int one, int two, int three, int four) {
        return (one < size && heap[one] < heap[hole]) || (two < size && heap[two] < heap[hole]) || (three < size && heap[three] < heap[hole]) || (four < size && heap[four] < heap[hole]);
    }
}
