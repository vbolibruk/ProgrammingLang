// Болібрук Влад
public class A_7_181 {
	public static void main(String[] args) {
		int arrL = 11, j;
		int[] arrOfa = {1, 2, 3, 4, 5, 6, 7, 8, 9, -5, -15};
		int sum = 0;

		for(int j2 = 0; j2 < arrL; j2++) {
			int i = j2 * j2;
			if(arrOfa[j2] % 5 == 0 && arrOfa[j2] % 2 != 0 && arrOfa[j2] < 0 && Math.abs(arrOfa[j2]) < i) {
				sum += arrOfa[j2];
			}
		}

		System.out.println("task is A_7_181");
		System.out.println("result  is " + sum);
	}
}