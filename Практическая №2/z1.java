// Определить сколько раз в этом массиве меняется знак. 
// Например, в массиве 1,-34, 8, 14, -5, -8, -78 , 3 знак меняется 4 раза.
	
public class z1 {
	public static void main(String n[]) {
		int[] array = {1, -3, -5, 3, -6, 2};
		int count = 0;
		for (int i = 1; i < array.length; i++) {
			if ((array[i - 1] < 0 && array[i] > 0) || (array[i - 1] > 0 && array[i] < 0)) {
				count++;
			}
		}
	System.out.println("Количество изменений знака: " + count);
	}
}
