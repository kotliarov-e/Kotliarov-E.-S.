//Реализовать программу, получающую на вход в качестве аргумента имя человека 
//и выводящую "Hello " + имя, в противном случае, если параметр не передавался, "Hello world".

public class z1 {
    public static void main(String name[]) {
    	if(name.length > 0) {
    		System.out.println("Hello " + name[0]);
    	}
    	else {
    		System.out.println("Hello world");   
    	}
    }
}
