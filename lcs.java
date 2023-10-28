
public class LCS 
{
    public static void main(String[] args) 
    {
        //test it works 
        /*String n1 = "mangoes";
        String n2 = "mementos";

        //check if the same string it still works
        //String n1 = "mangoes";
        //String n2 = "mangoes";
  
        String ret = LCS(n1, n2);
        System.out.println(ret);*/

        char[] alphabet = {'a','b','c','d','e','f','g','h',
                           'i','j','k','l','m','n','o','p', 
                           'q','r','s','t','u','v','w','x','y','z'};

        //test strings at different length and time it.
        int points = 0;
        for(points = 10; points<=100000; points = points*10)
        {
            String n1 = "";
            String n2 = "";
            //randim cahr generator to create random strings of lengths by 10. 
            for(int i=0; i<points; i++)
            {
                int random = (int)Math.random();
                n1 += alphabet[(random % 26)]; 
                int random2 = (int)Math.random();
                n2 += alphabet[(random2 % 26)]; 
            }
            long startT = System.nanoTime();
            String ret = null;
            ret = LCS(n1,n2);
            long endT = System.nanoTime();
            System.out.println("Alorithm at " + points + " takes " + (endT - startT));
        }
    
    }
    
   public static String LCS(String one, String two)
   {
        //get length of strings
        int len1 = one.length();
        int len2 = two.length();

        //create a double array 
        int[][] dArray = new int[len1][len2];

        // Build double array to mark the longest common subsequence as shown in class example
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if (one.charAt(i) == two.charAt(j)) {
                    dArray[i][j] = dArray[i][j] + 1;
                } else {
                    dArray[i][j] = Math.max(dArray[i][j], dArray[i][j]);
                }
            }
        }

        // Reconstruct the string from the double array
        StringBuilder ret = new StringBuilder();
        while ((len1 > 0) && (len2 > 0)) 
        {
            if (one.charAt(len1 - 1) == two.charAt(len2 - 1)) 
            {
                ret.insert(0, one.charAt(len1 - 1));
                len1--;
                len2--;
            } 
            else if (dArray[len1 - 1][len2] > dArray[len1][len2 - 1]) {
                len1--;
            } 
            else 
            {
                len2--;
            }
        }
        
        String result = ret.toString();
        return result;
   }

}
