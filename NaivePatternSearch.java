class NaivePattern {

	/**
	 * Author: Gaurav Shrivastava
	 */
	
	
	private static int PatternSearch(char[]text , char[] pattern){
		for (int i = 0; i <= text.length - pattern.length; i++)
	    {
	        int j;
	  
	        /* For current index i, check for pattern match */
	        for (j = 0; j < pattern.length; j++)
	        {
	            if (text[i+j] != pattern[j])
	                break;
	        }
	        if (j == pattern.length)  // if pat[0...M-1] = txt[i, i+1, ...i+M-1]
	        {
	           System.out.println("Pattern found at index " + i);
	        }
	    }
		return 0;
	}
	
	//Driver Program
	public static void main(String[] args) {
			String txt = "AABAACAADAABAAABAA";
			String pat = "AABAAC";
		    PatternSearch(txt.toCharArray(), pat.toCharArray());

	}

}
