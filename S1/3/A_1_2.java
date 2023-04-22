// Болібрук Влад 

public class A_1_2 {
	public static void main(String[] args) {
		int x = -1;
		int y = 1;

		float result = (Math.abs(x) - Math.abs(y)) / (1 + Math.abs(x * y));

		System.out.println("task is A_1_2");
		System.out.printf("result is %f\n", result);
	}
}
