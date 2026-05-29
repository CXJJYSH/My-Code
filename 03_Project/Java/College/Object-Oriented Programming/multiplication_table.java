public class multiplication_table {
    public class LowerTriangleMultiplicationTable {
        public static void main(String[] args) {
            for (int i = 0; i <= 9; i++) {
                for (int j = 0; j <= i; j++) {
                    int product = i * j;
                    if (product < 10) {
                        System.out.print("  " + product);
                    } else {
                        System.out.print(" " + product);
                    }
                }
                System.out.println();
            }
        }
    }
}

// 2026 05 28 11:13