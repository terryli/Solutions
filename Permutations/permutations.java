/*
 * Write a function that takes a string and returns all UNIQUE permutations.
 *
 * Difficulty: 3/5
 */

import java.util.Hashtable;
import java.util.Iterator;

public class permutations {

    static void permute(int runs, String word, boolean used[], 
			String input, Hashtable words) {
        if (runs > 0) {
            for (int i = 0; i < input.length(); i++) {
		if (!used[i]) {
		    used[i] = true;
		    permute(runs - 1, 
			    word + input.charAt(i),
			    used,
			    input,
			    words);
		    used[i] = false;
		}
            }
	} else {
	    words.put(word, true);
	}
    }

    public static void main(String[] args) {
        String input = args[0];
	Hashtable words = new Hashtable();

	boolean used[]= new boolean[input.length()];
	for (int i = 0; i < input.length(); i++) {
	    used[i] = false;
	}

        permute(input.length(), "", used, input, words);
	Iterator keys = words.keySet().iterator();
	while (keys.hasNext()) {
	    System.out.println(keys.next());
	}
    }
}