package prakt3;

public class Data {
	public static void main(String[] args) {
		Library library = new Library("Название Библиотеки", "Название комнаты", "Фамилия", 
				"Название книги", "20.01.2016", 31, 1000);
		
		System.out.println(library.toString());
	}
}
