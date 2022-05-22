// Дан массив х(n). Переписать в массив у(n) элементы массива х, большие 3. (со сжатием., без пустых элементов внутри) 
// Затем упорядочить методом «выбора и перестановки» по возрастанию новый массив.

public class z2 {
	public static void main(String n[]) {
		int[] arrayX = {1, -3, -5, 4, -2, 6, 8};
		int[] arrayTemp = new int[arrayX.length];
		int[] arrayY = new int[arrayX.length];
		int count = 0;

		for (int i = 1; i < arrayX.length; i++) {
			if(arrayX[i] > 3) {
				arrayTemp[i] = arrayX[i];
			}
		}
		for (int min = 0; min < arrayTemp.length; min++) {	//Сортировка по возрастанию
			int least = min;
			for (int j = min + 1; j < arrayTemp.length; j++) {
				if (arrayTemp[j] < arrayTemp[least]) {
					least = j;					
				}
			}
			int temp = arrayTemp[min];
			arrayTemp[min] = arrayTemp[least];
			arrayTemp[least] = temp;
		}
		
		for (int i = 1; i < arrayTemp.length; i++) {
			if (arrayTemp[i] > 3) {
				arrayY[i - count] = arrayTemp[i];
			}
			else {
				count++;
			}
		}
		
		for (int i = 1; i < arrayY.length; i++) {
			System.out.print(arrayY[i] + " ");
		}
	}
}
