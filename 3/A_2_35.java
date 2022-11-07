// Болібрук Влад 

public class A_2_35 {
	public static void main(String[] args) {
		int x = 1;
		int y = 2;
		int z = 3;

		int sum = x + y + z;
		int mult = x * y * z;
		int max = maxF(sum, mult);
		int min = minF(x + y + z / 2, x * y * z) * minF(x + y + z / 2, x * y * z) + 1;

		System.out.println("task is A_2_35");
		System.out.println("result max is " + max);
		System.out.println("result min is " + min);
	}

	public static int minF(int a, int b) {
		return a > b ? b : a;
	}

	public static int maxF(int a, int b) {
		return a > b ? a : b;
	}
}