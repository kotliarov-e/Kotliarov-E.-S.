public class z3 {
	public static void main(String n[]) {
		int i1 = Integer.parseInt(n[0]), 
		    i2 = Integer.parseInt(n[1]);
	    if(n.length == 2) {
		    System.out.println(n[0] + " + " + n[1] + " = " + (i1 + i2));
	    }
	    else {
	    	System.out.println("Неверное количество параметров");
	    }
	}
}