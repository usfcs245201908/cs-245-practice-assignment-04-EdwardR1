public class SelectionSort implements SortingAlgorithm {

    private void swap(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

    private int findMin(int[] arr, int start) {
        int min = start;
        for (int i = start + 1; i < arr.length; i++) {
            if (arr[i] < arr[min]) {
                min = i;
            }
        }
        return min;
    }

    public void sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            swap(a, i, findMin(a, i));
        }
    }

}