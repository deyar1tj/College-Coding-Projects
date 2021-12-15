import java.io.FileReader;
import java.util.Scanner;

public class TheBank {

	public static void main(String[] args) {
		
		 	int time=0;
		    Scanner in = new Scanner(new FileReader("yesterday.txt"));
		    
		    Customer a,b,c;
		    OrderedList events = new OrderedList(500);
		    Queue line = new Queue(500);
		    int i=0;
		    while (in.hasNext()){
		      
		      
		      i++;
		      Customer cust = new Customer(i,in.nextInt(),in.nextInt());
		      Event arrival = new Event('A',time,cust);
		      time = cust.getArrivalTime();
		      events.insert(arrival);
		      
		      while (!events.isEmpty()){
		        Event current = events.give();
		        
		        
		        if (current.getEventType() == 'A'){
		          System.out.println(current.getCustomer().getCustomer_ID() + " has arrived at "+ current.getCustomer().getArrivalTime());
		          boolean atFront = line.isEmpty();
		          line.enqueue(current.getCustomer());
		         
		          
		          if (atFront){
		            Event dep = new Event('D',((current.getCustomer()).getTransactionTime()+ time),current.getCustomer());
		            events.insert(dep);
		            
		          }
		          
		          if (!atFront){
		            cust = new Customer(i,in.nextInt(),in.nextInt());
		            arrival = new Event('A',time,cust);
		            events.insert(arrival);
		            
		          }
		        }
		       else if (current.getEventType() == 'D'){
		          line.dequeue();
		          System.out.println(current.getCustomer().getCustomer_ID()+ " leaves at " + current.getEventTime());
		          events.delete(1);
		          events.delete(1);
		          
		          
		          if(!line.isEmpty()){
		            current = events.give();
		            Event dep = new Event('D',((current.getCustomer()).getTransactionTime()+ time),current.getCustomer());
		            events.insert(dep);
		            
		          }          
		        }
		        
		      }
		    }
		  }
}
