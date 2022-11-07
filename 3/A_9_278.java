// Болібрук Влад
public class A_9_278 {
	public static void main(String[] args) {
		int[] arrOfn = new int[20];
		int[] arrOfx = new int[20];
		int result;
		int a = 0, b = 0;
		for(int j = 0; j < 20; j++) {
			arrOfn[j] = j;
		}

		for(int j = -10; j < 10; j++) {
			arrOfx[j] = j;
		}
		for(int j = 0; j < 20; j++) {
			a += arrOfn[j] * arrOfx[j];
			b += arrOfn[j];
		}

		System.out.println("task is A_9_278");
		System.out.println("result is " + (a / b));
	}
}