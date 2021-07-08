import java.util.Scanner;

public class mergeSort {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        System.out.println("Enter the size of the array: ");
        int arrSize = scanner.nextInt();
        int[] arr = getIntegers(arrSize);
        printArray(sortIntegers(arr));
    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    public static int[] getIntegers(int size) {
        int[] values = new int[size];
        System.out.println("Enter " + size + " values: ");
        for (int i = 0; i < values.length; i++) {
            values[i] = scanner.nextInt();
        }

        return values;
    }

    public static int[] sortIntegers(int[] arr) {
        if (arr.length == 1) {
            return arr;
        }
        int mid = (arr.length / 2);
        int[] b = sortIntegers(slice(arr, 0, mid));
        int[] c = sortIntegers(slice(arr, mid, arr.length));
        return merge(b, c);
    }

    public static int[] slice(int[] arr, int startInd, int stopInd, int step) {
        int[] newArray = new int[stopInd - startInd];
        for (int i = startInd; i < stopInd; i += step) {
            newArray[i - startInd] = arr[i];
        }
        return newArray;
    }

    public static int[] slice(int[] arr, int startInd, int stopInd) {
        return slice(arr, startInd, stopInd, 1);
    }

    public static int[] merge(int[] b, int[] c) {
        int p = 0, q = 0;
        int[] mergedArray = new int[b.length + c.length];
        int mergedInd = 0;
        while (p < b.length && q < c.length) {
            if (b[p] < c[q]) {
                mergedArray[mergedInd] = b[p];
                p++;
                mergedInd++;
            } else {
                mergedArray[mergedInd] = c[q];
                q++;
                mergedInd++;
            }
        }
        while (p < b.length) {
            mergedArray[mergedInd] = b[p];
            mergedInd++;
            p++;
        }
        while (q < c.length) {
            mergedArray[mergedInd] = c[q];
            mergedInd++;
            q++;
        }

        return mergedArray;
    }
}

