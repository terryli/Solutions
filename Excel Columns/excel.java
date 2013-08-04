/*
 * Write a method that takes an excel column id (A,B,C,D…AA,AB,AC,… AAA..)
 * and returns the associated column number (A=1,B=2,… AA=26..).
 *
 * Difficulty: 2/5
 */

public class excel {

    public static void main(String[] args) {
	int offset = 9;
	int factor = 26;
	int sum = 0;
	    
	char[] charList = args[0].toCharArray();
	for (int i = 0; i < charList.length; i++) {
	    int value = Character.getNumericValue(charList[i]);
	    sum = sum * factor + (value - offset);
	}
	System.out.println(sum);
    }

}
