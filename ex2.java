public class impStack {
	
	
	int logicalsize = 0;
	int top = -1;
	
	void Stack(String wrd)
	{
		int count = 0;
		char charin;
	
		while(count < wrd.length()){
			charin = wrd.charAt(count);
			System.out.println(charin);
			arr[count] = charin;
			this.top++;
			count++;
		}
	}
	
	public void push(char chars)
	{
		
	}
	
	public char pop()
	{
		char retval;
		retval = arr[logicalsize];
		return retval;
		
	}

	public char top()
	{
		return('\n');
	}
	
	public boolean isempty()
	{
		return false;
	}
	
	public boolean isfull()
	{
		return false;
	}
}
