
public class EightQueens {
    static int N = 8;
    static int[] board = new int[N];

    static boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col ||
                Math.abs(board[i] - col) == Math.abs(i - row)) {
                return false;
            }
        }
        return true;
    }

    static boolean solve(int row) {
        if (row == N) {
            return true;
        }

        for (int col = 0; col < N; col++) {
            if (isSafe(row, col)) {
                board[row] = col;

                if (solve(row + 1)) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        if (solve(0)) {
            System.out.println("Solution:");
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (board[i] == j)
                        System.out.print("Q ");
                    else
                        System.out.print(". ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No solution");
        }
    }
}
