import java.util.Scanner;

public class prog9of10 {

	public static void main(String[] args) {
		Scanner scn1 = new Scanner(System.in);

		int sum = 0;
		int count = 0;
		int avg = 0;
		int min = 9999;
		int max = -9999;
		int nums = 0;
		int ary1[] = new int[100];
	
		System.out.println("Enter a number:");
		
		while(scn1.hasNext()){
			ary1[nums] = scn1.nextInt();
			
			
			min = mymin(nums, min);
			max = mymax(nums, max);
			sum = mysum(nums, sum);
			count = mycount(nums, count);
			
			

		}
	

		avg = sum / count;

		System.out.println("The sum is: " + sum);
		System.out.println("The count is: " + count);
		System.out.println("The average is: " + avg);
		System.out.println("The minimum is: " + min);
		System.out.println("The maximum is: " + max);
	
	}


	public static int mysum(int newnum, int sum){
		sum = newnum + sum;
		return sum;
	}
	public static int mycount(int newnum, int count){
		count++;
		return count;
	}


	public static int mymin(int newnum, int min){
		
		if(newnum < min){
			min = newnum;
		}
		return min;
		
	}
	public static int mymax(int newnum, int max){
		
		if(newnum > max){
			max = newnum;
		}
		return max;
		
	}
}


