package prakt2;



public class z3 {
	public static void main(String n[]) {
		int[][] array = new int[5][5];
		
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array.length; j++) {
				array[i][j] = (int)(Math.random()*20 - 10);
			}
		}
		
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array.length; j++) {
				System.out.print(array[i][j] + " ");
			}
			System.out.println();
		}
		
		int[] tempVector = new int[array[0].length]; // создаем вектор
		double[] temp = new double[array[0].length];
        for (int i = 0; i < array[0].length; i++) { // гоняем цикл по колличеству столбцов входящей матрицы
                        
            for (int j = 0; j < array.length; j++) { // гоняем цикл по колличеству строк входящей матрицы
                
                if (array[j][i] > 0) {  
                    tempVector[i] *= array[j][i]; // суммируем положительные элементы                 
                }    
            }
            temp[i] = (Math.sqrt(tempVector[i])); // считаем среднеарифмитическое
        }
        
        System.out.println("Вектор В:");      
        for (double i : temp)
            System.out.print(Math.round(i) + " ");
	}
}
