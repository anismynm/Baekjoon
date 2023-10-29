import java.util.Scanner;

public class VerticalReading_10798 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		char arr[][] = new char[5][15];
		String input;
		for (int i = 0; i < 5; i ++) {
			input = scan.next();
			for (int j = 0; j < input.length(); j ++) {
				arr[i][j] = input.charAt(j);
			}
		}
	
		for (int i = 0; i < 15; i ++) {
			for (int j = 0; j < 5; j ++) {
				if (arr[j][i] != 0) {
					System.out.print(arr[j][i]);
				}
			}
		}
		System.out.println();
		scan.close();
	}

}
