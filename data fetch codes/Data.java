/*Used to fetch the distance and time matrices using google maps api
*Which will be used for deciding the tours
*/
import static java.lang.System.exit;
import org.json.*;
import java.net.*;
import java.util.*;
public class Data
{
    public double dist_val[][]=new double[20][20];//stores the distances from the map
    public double dur_val[][]=new double[20][20];//stores the durations from the map
    public void fetch() throws Exception
    {
      String s[]=new String[4];//stores the urls for fetching data, 100 elements at a time
      s[0]="https://maps.googleapis.com/maps/api/distancematrix/json?units=si&origins=Darjeeling|DalLake|Jaisalmer|Kolkata|JimCorbett|Mussoorie|Beas|Kutch|Delhi|Kaziranga&destinations=Darjeeling|DalLake|Jaisalmer|Kolkata|JimCorbett|Mussoorie|Beas|Kutch|Delhi|Kaziranga&key=AIzaSyAKK-s2APy7EYEmpSADb9in2EtApPPhr0Q";
      s[1]="https://maps.googleapis.com/maps/api/distancematrix/json?units=si&origins=Darjeeling|DalLake|Jaisalmer|Kolkata|JimCorbett|Mussoorie|Beas|Kutch|Delhi|Kaziranga&destinations=Gulmarg|Kanyakumari|Bikaner|Mumbai|Bandipur|Manali|GurudongmarLake|LadakhVacation|Chennai|GirNationalPark&key=AIzaSyAKK-s2APy7EYEmpSADb9in2EtApPPhr0Q";
      s[2]="https://maps.googleapis.com/maps/api/distancematrix/json?units=si&origins=Gulmarg|Kanyakumari|Bikaner|Mumbai|Bandipur|Manali|GurudongmarLake|LadakhVacation|Chennai|GirNationalPark&destinations=Darjeeling|DalLake|Jaisalmer|Kolkata|JimCorbett|Mussoorie|Beas|Kutch|Delhi|Kaziranga&key=AIzaSyAKK-s2APy7EYEmpSADb9in2EtApPPhr0Q";
      s[3]="https://maps.googleapis.com/maps/api/distancematrix/json?units=si&origins=Gulmarg|Kanyakumari|Bikaner|Mumbai|Bandipur|Manali|GurudongmarLake|LadakhVacation|Chennai|GirNationalPark&destinations=Gulmarg|Kanyakumari|Bikaner|Mumbai|Bandipur|Manali|GurudongmarLake|LadakhVacation|Chennai|GirNationalPark&key=AIzaSyAKK-s2APy7EYEmpSADb9in2EtApPPhr0Q";
      int c=0;
      int i,j;
      /*storing the data into distance and duration matrices by parsing the json file received*/
      while(c<4)
      {
        URL url = new URL(s[c]);
        Scanner sc=new Scanner(System.in);
        String str = null;
             try (Scanner scan = new Scanner(url.openStream()))
             {
                 str = new String();
                 while (scan.hasNext())
                     str += scan.nextLine();
             }
             catch (Exception e)
             {
                 System.out.println("No Internet Connection");
                 sc.nextLine();
                 exit(0b1);
             }
         JSONObject obj = new JSONObject(str);
         if (! obj.getString("status").equals("OK"))
         {
             System.out.println(obj.getString("status"));
             sc.nextLine();
             System.exit(0);
         }
         int ini,inj;
         ini=(c/2)*10;
         inj=(c%2)*10;
         for(i=ini;i<ini+10;i++)
         {
           String str1 = obj.getJSONArray("rows").get(i%10).toString();
           JSONObject obj1=new JSONObject(str1);
           for(j=inj;j<inj+10;j++)
           {
             String str2= obj1.getJSONArray("elements").get(j%10).toString();
             JSONObject obj2=new JSONObject(str2);
             dist_val[i][j]= obj2.getJSONObject("distance").getInt("value")/1000.0;//converting distance to km
             dist_val[i][j]=(dist_val[i][j]<1)?999999:dist_val[i][j];
             dur_val[i][j]= obj2.getJSONObject("duration").getInt("value")/86400.0;//converting time to days
             dur_val[i][j]=(dur_val[i][j]<1e-6)?999999:dur_val[i][j];
           }
         }
         c++;
      }
      /*printing the results*/
      System.out.println("DISTANCE MATRIX(km):--->");
      for(i=0;i<20;i++)
      {
        for(j=0;j<20;j++)
           System.out.printf("%.4f ",dist_val[i][j]);
        System.out.println();
      }
      System.out.println("DURATION MATRIX(days):--->");
      for(i=0;i<20;i++)
      {
        for(j=0;j<20;j++)
            System.out.printf("%.4f ",dur_val[i][j]);
        System.out.println();
      }
    }
}
