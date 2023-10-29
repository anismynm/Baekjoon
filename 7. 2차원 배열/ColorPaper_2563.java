import java.util.Scanner;

public class ColorPaper_2563 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int cnt = scan.nextInt();
		int array[][] = new int[100][100];
		int result = 0;

		for (int i = 0; i < cnt; i ++) {
			int x = scan.nextInt();
			int y = scan.nextInt();
			for (int j = x; j < x + 10; j ++) {
				for (int k = y; k < y + 10; k ++) {
					array[j][k] = 1;
				}
			}
		}

		for (int i = 0; i < 100; i ++) {
			for (int j = 0; j < 100; j ++) {
				if (array[i][j] == 1) {
					result++;
				}
			}
		}
		System.out.println(result);
		scan.close();
	}

}
