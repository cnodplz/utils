import java.io.*; 
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class CR2 {

    // set variables
    List<List<String>> lines = new ArrayList<>();
    int rows = 21;
    int columns = 20;
    int iterationCount = 0;

    public CR2(String[] args) {
        // read file, scanners
        File file = null;
        try {
            if (args.length > 0) {
                String fileName = args[0];
                file = new File(fileName);
            }
            else {
                file = new File("Crime.csv");
            }
        } catch (Exception e) {
    		e.printStackTrace();
        }

        // read crimedata
        try {
            Scanner inputStream = new Scanner(file);
            while(inputStream.hasNext()) {
                String line= inputStream.nextLine();
                String[] values = line.split(",");
                // this adds the currently parsed line to the 2-dimensional string array
                this.lines.add(Arrays.asList(values));
            } 
            inputStream.close();
        } catch (FileNotFoundException e) {
			e.printStackTrace();
        }
    }

    public void getSummary() {
        // iterate and print crimedata 2-dimensional arraylist
        System.out.println("\nCrime Statistics:\n");
        int lineNo = 1;
        for(List<String> line: this.lines) {
            int columnNo = 1;
            for (String value: line) {
                System.out.println("Line " + lineNo + " Column " + columnNo + ": " + value);
                columnNo++;
            }
            lineNo++;
        }
    }

    public void getMaxMurder() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(5));
            if (mHold > mRate) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }

    public void getMinMurder() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(5));
            if (mHold < mRate || mRate == 0) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }
    
        public void getMaxRobbery() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(9));
            if (mHold > mRate) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }

    public void getMinRobbery() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(9));
            if (mHold < mRate || mRate == 0) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }
    
        public void getMaxRa() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(7));
            if (mHold > mRate) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }

    public void getMinRa() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(7));
            if (mHold < mRate || mRate == 0) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }
    
        public void getMaxVC() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(7));
            if (mHold > mRate) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }

    public void getMinVC() {
        float mRate = 0;
        float mHold = 0;
        int mYear = 0;
        for (int y=1; y<21; y++){
            mHold = Float.parseFloat(lines.get(y).get(7));
            if (mHold < mRate || mRate == 0) {
                mRate = mHold;
                mYear = y;
            }
        }
        System.out.println("Year: " + lines.get(mYear).get(0) + "\nRate: " + mRate);
    }
    
    public void getPopGrowth() {
		//Population growth in percentages from each consecutive year (e.g. 1994-1995
		//calculation is ((262803276 - 260327021)/260327021)*100 = 0.9512%, 1995-1996 would
		//be ((265228572 - 262803276)/262803276)*100 = 0.9229%)
		float mRate = 0;
        float mHold1 = 0;
        float mHold2 = 0;
		float mPercent = 0;
        int mYear = 0;
        for (int y=1; y<20; y++){
            mHold1 = Float.parseFloat(lines.get(y).get(1));
            mHold2 = Float.parseFloat(lines.get(y+1).get(1));
            mPercent = ((mHold2 - mHold1)/mHold1)*100;
			System.out.println("Years: " + lines.get(y).get(0) + "-" + lines.get(y+1).get(0) + "\n" + mPercent + "%");
        }
	}

    /*public static void main(String[] args) {
        CR2 myRdr = new CR2(args);
        //myRdr.getSummary();
        myRdr.getMaxMurder();
    }*/

// end CR2 class  
} 
