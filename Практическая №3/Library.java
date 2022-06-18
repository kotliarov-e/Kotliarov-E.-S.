//создать программу для определения класса в некоторой предметной области.
//Описать свойства, конструктор,
//методы геттеры/сеттеры, перекрыть метод toString() для вывода полной
//информации об объекте в отформатированном виде.

package prakt3;

public class Library {
	private String LibraryName;
	private String ReadingRoomName;
	private String ReaderLastName;
	private String BookName;
	private String DateOfExtradition;
	private int TermOfExtradition;
	private int DepositAmount;
	
	Library(String libraryName, String ReadingRoomName, String ReaderLastName, String BookName,
		      String DateOfExtradition, int TermOfExtradition, int DepositAmount) {
		    this.LibraryName = libraryName;
		    this.ReadingRoomName = ReadingRoomName;
		    this.ReaderLastName = ReaderLastName;
		    this.BookName = BookName;
		    this.DateOfExtradition = DateOfExtradition;
		    this.TermOfExtradition = TermOfExtradition;
		    this.DepositAmount = DepositAmount;
	}
	
	 public String toString(){
	        return "Название библиотеки: " + LibraryName +
	                "\nНазвание читательского зала: " + ReadingRoomName +
	                "\nФамилия читателя: " + ReaderLastName +
	                "\nНазвание литературы: " + BookName +
	                "\nДата Выдачи: " + DateOfExtradition +
	                "\nСрок выдачи: " + TermOfExtradition +
	        		"\nСумма залога: " + DepositAmount;
	 }
}
