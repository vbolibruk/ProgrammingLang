// Болібрук Влад 

public class A_4_81 {
	public static void main(String[] args) {
		int x = 1;
		int a = 2;
		int n = 3;
		int j, result = 1;

		if(n == 1) {
			result = (x + a) * (x + a);
		} else {
			for(int j2 = 0; j2 < n; j2++) {
				result = (result + 2) * (result + 2);
			}
		}
		result = result + 2;

		System.out.println("task is A_4_81");
		System.out.println("result  is " + result);
	}
}
