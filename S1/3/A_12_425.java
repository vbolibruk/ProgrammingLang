// Болібрук Влад
public class A_12_425 {
	public static void main(String[] args) {
		float s = -10;
		float t = 20;
		float result = calculateRes(1.2f, s) + calculateRes(t, s) - calculateRes(2 * s - 1, s * t);


		System.out.println("task is A_12_425");
		System.out.printf("result is %f\n", result);
	}

	public static float calculateRes(float a, float b) {
		return (a * a + b * b) / (a * a + 2 * a * b + 3 * b * b + 4);
	}
}