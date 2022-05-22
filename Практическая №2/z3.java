// Определить матрицу (двумерный массив) и ее заполнить случайными значениями.
// Построить вектор B, который возвращает среднее геометрическое положительных 
// элементов в каждом столбце матрицы

public class z3 {
  public static void main(String n[]) {
    double[][] array = new double[5][5];

    for (int i = 0; i < array.length; i++) {
      for (int j = 0; j < array.length; j++) {
        array[i][j] = (double)(Math.round(Math.random()*20 - 10));
        System.out.print(Math.round(array[i][j]) + "  ");
      }
      System.out.println();
    }

    double[] tempVector = new double[array.length];
    double count;
        for (int i = 0; i < array.length; i++) {  
        	count = 0;
        	tempVector[i] = tempVector[i] + 1;
          for (int j = 0; j < array.length; j++) {
                if (array[j][i] > 0) {  
                	count++;         	
                    tempVector[i] *= array[j][i]; 
                }
          }
          tempVector[i] = Math.pow(tempVector[i], 1 / count);
        }

        System.out.println("Вектор В:");      
        for (double i : tempVector)
            System.out.print(Math.round(i) + " | ");
  }
}
