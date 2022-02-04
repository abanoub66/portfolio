public class QuickSort {
    private static final int CUTOFF = 20;

    public static void quickSort(int[] arr, int left, int right) {
        if (left + CUTOFF <= right) {
            int pivot = median3(arr, left, right);
            int i = left;
            int j = right - 1;
            for (; ; ) {
                while (arr[++i] < pivot) {
                }
                while (arr[--j] > pivot) {
                }
                if (i < j) {
                    swap(arr, i, j);
                } else {
                    break;
                }
            }
            swap(arr, i, right - 1);

            quickSort(arr, left, i);
            quickSort(arr, i + 1, right);
        } else {
            insertionSort(arr, left, right);
        }
    }

    private static void insertionSort(int[] arr, int left, int right) {
        int j;
        for (int i = left + 1; i <= right; i++) {
            int temp = arr[i];
            for (j = i; j > left && temp < arr[j - 1]; j--) {
                arr[j] = arr[j - 1];
            }
            arr[j] = temp;
        }
    }

    private static int median3(int[] arr, int left, int right) {
        int mid = (left + right) / 2;
        if (arr[mid] < arr[left]) {
            swap(arr, left, mid);
        }
        if (arr[right] < arr[left]) {
            swap(arr, left, right);
        }
        if (arr[right] < arr[mid]) {
            swap(arr, mid, right);
        }
        swap(arr, mid, right - 1);
        return arr[right - 1];
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
