// Дан двумерный массив А, размером (n×n) (или квадратная матрица А). 
// Найти среднее арифметическое положительных элементов параллели главной диагонали, 
// расположенной выше над диагональю.

public class z4 {
	public static void main(String n[]) {
		int n1 = 5;
		int[][] array = new int[n1][n1];
		double sum = 0, sar = 0;
		int count = 0;
		
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array.length; j++) {
				array[i][j] = (int)(Math.random()*20 - 10);
				System.out.print(array[i][j] + "  ");
			}
			System.out.println();
		}
		
        for (int i = 0; i < array.length; i++) {        	
        	for (int j = 0; j < array.length; j++) {
        		if ((array[i][j] > 0) && (i < j) && (j - i == 1)) {  
                	count++;
                    sum += array[i][j]; 
                }
            }
        }
		
        if (count > 0) {
    		sar = sum / count; 
    	}
        System.out.println("Среднее арифметическое параллели главной диагонали: " + sar);      
	}
}
