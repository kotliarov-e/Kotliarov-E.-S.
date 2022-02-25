public class z4 {
	public static void main(String n[]) {
	    String login = "Ivan", password = "1122";
	    if((n[0].equals(login)) & (n[1].equals(password))) {
	    	System.out.println("Вас узнали. Добро пожаловать, " + login + ".");
	    }
	    else {
	    	System.out.println("Логин и пароль не распознаны. Доступ запрещен.");
	    }
    }
}
