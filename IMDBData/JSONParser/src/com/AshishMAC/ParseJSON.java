package com.AshishMAC;
import java.io.*;
import java.net.*;
import org.json.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class ParseJSON {

	public static void main(String[] args)  throws FileNotFoundException {
		if (args.length < 1) {
			System.out.println(" Kindly provide input in the following format :");
			System.out.println(" ParseJSON <directory-location-containing-Movie-List-Text-File>");
			System.exit(1);
		} 
		String path = args[0];int count=0;
		BufferedReader br = null;String line;
		File file =new File(path+"/MovieList.txt");
		File file2 = new File(path+"/MovieDetail.csv");
		PrintWriter pw = new PrintWriter(file2);
        StringBuilder sb = new StringBuilder();
        sb.append("Title");sb.append(',');
        sb.append("imdbID");sb.append(',');
        sb.append("Actors");sb.append(',');
        sb.append("Director");sb.append(',');
        sb.append("Released");sb.append(',');
        sb.append("Rated");sb.append(',');
        sb.append("BoxOffice");sb.append(',');
        sb.append("IMDB Votes");sb.append(',');
        sb.append("Genre");sb.append(',');
        sb.append("imdbRating");sb.append(',');
        sb.append("Plot");sb.append(',');
        sb.append('\n');
        
        try {
            br = new BufferedReader(new InputStreamReader(new FileInputStream(file), "Cp1252"), 100);
            while ((line = br.readLine()) != null) {
            	String boxOffice= "N/A",title =line,id ="N/A",actors ="N/A",directors ="N/A",release ="N/A",contentRating ="N/A",votes ="N/A",genre ="N/A",Rating ="N/A",plot ="N/A";
        		String movie_name=line;
        		String result = getURLContent ("http://www.omdbapi.com/?t="+movie_name.replace(" ","%20"));
        		JSONObject obj = new JSONObject(result);
        		count=count+1;
        		System.out.println(count+":"+movie_name);
        		if (obj.has("Title")) {
        			title = obj.getString("Title").replaceAll(",",";");
        			if (obj.has("imdbID")) {
        				id= obj.getString("imdbID").replaceAll(",",";");}
        			if (obj.has("Actors")) {
        				actors= obj.getString("Actors").replaceAll(",",";");}
        			if (obj.has("Director")) {
        				directors= obj.getString("Director").replaceAll(",",";");}
        			if (obj.has("Released")) {
        				release= obj.getString("Released").replaceAll(",",";");}
        			if (obj.has("Rated")) {
        			contentRating= obj.getString("Rated").replaceAll(",",";");}
        			if (obj.has("BoxOffice")) {
        				boxOffice= obj.getString("BoxOffice").replaceAll(",",";");}
        			if (obj.has("imdbVotes")) {
        			votes= obj.getString("imdbVotes").replaceAll(",",";");}
        			if (obj.has("Genre")) {
        			genre= obj.getString("Genre").replaceAll(",",";");}
        			if (obj.has("imdbRating")) {
        			Rating= obj.getString("imdbRating").replaceAll(",",";");}
        			if (obj.has("Plot")) {
        			plot= obj.getString("Plot").replaceAll(",",";");}
        		}
                sb.append(title);sb.append(',');
                sb.append(id);sb.append(',');
                sb.append(actors);sb.append(',');
                sb.append(directors);sb.append(',');
                sb.append(release);sb.append(',');
                sb.append(contentRating);sb.append(',');
                sb.append(boxOffice);sb.append(',');
                sb.append(votes);sb.append(',');
                sb.append(genre);sb.append(',');
                sb.append(Rating);sb.append(',');
                sb.append(plot);sb.append(',');
                sb.append('\n');
                pw.write(sb.toString());
                sb.setLength(0);
            }
            br.close();
        }catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        pw.close();
        System.out.println("done!");
	}


public static String getURLContent(String p_sURL)
{
    URL oURL;
    URLConnection oConnection;
    BufferedReader oReader;
    String sLine;
    StringBuilder sbResponse;
    String sResponse = null;
    try
    {
        oURL = new URL(p_sURL);
        oConnection = oURL.openConnection();
        oReader = new BufferedReader(new InputStreamReader(oConnection.getInputStream()));
        sbResponse = new StringBuilder();

        while((sLine = oReader.readLine()) != null)
        {
            sbResponse.append(sLine);
        }

        sResponse = sbResponse.toString();
    }
    catch(Exception e)
    {
        e.printStackTrace();
    }

    return sResponse;
}

}
