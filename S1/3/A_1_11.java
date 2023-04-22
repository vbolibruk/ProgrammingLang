// Болібрук Влад 
public class A_1_11 {
	public static void main(String[] args) {
		int x = 1;
		int y = 2;
		int z = 3;

		float resultA = (float)((Math.sqrt(Math.abs(x - 1)) - Math.pow(Math.abs(y), 1 / 3)) / (1 + (x * x) / 2 + (y * y) / 4));
		float resultB = (float)(x * (Math.atan(z) + Math.exp(-(x + 3))));

		System.out.println("task is A_1_11");
		System.out.printf("result is %f\n", resultA);
		System.out.printf("result is %f\n", resultB);
	}
}