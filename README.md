## Transactional Data Analysis

This repository provides code and instructions for analyzing transactional data. The analysis focuses on two questions: Question 1 and Question 2. For each question, both Pairs and Stripes approaches are implemented to compute co-occurrences of items in the dataset.

### Question 1: Pairs Approach

In the Pairs approach, the goal is to calculate the co-occurrences of each pair of items in the transactional data. The provided mapper.py and reducer.py files contain the code to accomplish this. The mapper generates key-value pairs in the format `<item1>_<item2>` to represent each pair, and the reducer aggregates the counts and computes the probability of co-occurrence.

To run the Pairs approach, follow these steps:
1. Execute the mapper and reducer using the Hadoop Streaming jar, providing the paths to the mapper.py and reducer.py files.
2. Specify the input path to the retail dataset and the output path for storing the results.
3. Use the `hadoop fs -get` command to retrieve the output file from HDFS and inspect the results.

### Question 1: Stripes Approach

The Stripes approach is an alternative method to calculate co-occurrences in transactional data. It uses a "Stripes" data structure, where each item is paired with a list of other items that co-occur with it. The mapper.py and reducer.py files provided in the repository implement this approach.

To run the Stripes approach, follow these steps:
1. Execute the mapper and reducer using the Hadoop Streaming jar, specifying the mapper.py and reducer.py file paths.
2. Set the input path to the retail dataset and the output path to store the results.
3. Retrieve the output file from HDFS using the `hadoop fs -get` command and examine the output.

### Question 2: Pairs Approach

Question 2 extends the analysis to compute the co-occurrence of triplets of items in the transactional data. Similar to Question 1, the Pairs approach is used to achieve this. The mapper.py and reducer.py files provided in the repository are designed for this purpose.

To run the Pairs approach for Question 2, follow the same steps as for Question 1 with appropriate file paths and output locations.

### Question 2: Stripes Approach

In the Stripes approach for Question 2, the mapper.py and reducer.py files are used to calculate the co-occurrence of triplets. The mapper.py file generates output in the format `<item1> <item2> <list[c1,c2,...]>`, where c1, c2, etc., represent the counts of item2 that co-occur with item1. The reducer.py file aggregates the counts and computes the probability of co-occurrence.

To run the Stripes approach for Question 2, follow the steps outlined in the repository, providing the appropriate file paths and output locations.

## Contributors

- [Your Name](https://github.com/yourusername)
## Exercise 1: Transactional Data Analysis

1. First, download the retail dataset from [http://fimi.ua.ac.be/data/](http://fimi.ua.ac.be/data/).

2. Unzip the file using the following command:
   ```
   gzip -d retail.data.gz
   ```

3. Create the HDFS directory that will serve as the input file storage location:
   ```
   hadoop fs -mkdir -p /user/your/path/transaction/input
   ```

4. Copy the downloaded dataset into the above directory:
   ```
   hadoop fs -put /your/path/to/retail.data /user/your/path/transaction/input
   ```

Now, we can start with Question 1.

### Question 1: Pairs Approach

In this approach, we will compute the co-occurrences of each pair of items.

1. Mapper.py: Code in respective files

2. Reducer.py: Code in respective files

3. Execute the mapper and reducer using the following command:
   ```
   hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -reducer /your/path/to/reducer.py -input /user/your/path/transaction/input/retail.data -output /user/your/path/transaction/q1pairs10
   ```

4. Get the output with the following command:
   ```
   hadoop fs -get /user/your/path/transaction/q1pairs10
   ```

   Open the output file to see the results.

### Question 1: Stripes Approach

In the stripes approach, the key-value pair is in the format <item1> list[item2, item3, ...].

1. Mapper.py: Code in respective files

2. Reducer.py: Code in respective files

3. Execute the mapper and reducer using the following command:
   ```
   hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -reducer /your/path/to/reducer.py -input /user/your/path/transaction/input/retail.data -output /user/your/path/transaction/q1stripe5
   ```

4. Fetch the output file from HDFS using the following command:
   ```
   hadoop fs -get /user/your/path/transaction/q1stripe5
   ```

   Check the output by opening the output file.

Output: (Output details not provided)

If you encounter the "Container is running beyond limits" error, add the following configuration in the mapred-site.xml file to resolve it.

### Question 2: Pairs Approach

In this question, we need to compute the co-occurrence of each triplet of items.

1. Mapper.py: Code in respective files

2. Reducer.py: Code in respective files

3. Execute the mapper and reducer using the following command:
   ```
   hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -reducer /your/path/to/reducer.py -input /user/your/path/transaction/input/retail.data -output /user/your/path/transaction/temp11 -file /your/path/to/Ques1_pair
   ```

4. Fetch the output file from HDFS using the following command:
   ```
   hadoop fs -get /user/your/path/transaction/temp11
   ```

   Check the output by opening the output file.

### Question 2: Stripes Approach

1. Create the input folder:
   ```
   hadoop fs -mkdir -p /user/your/path/transaction/input
   ```

2. Put the input file into the input folder:
   ```
   hadoop fs -put /your/path/to/retail.data /user/your/path/transaction/input
   ```

3. Mapper.py: Code in respective files

4. Reducer.py: Code in respective files

5. Execute the mapper and reducer using the following command:
   ```
   hadoop jar /your/path/to/hadoop-streaming-2.8.0.jar -file /your/path/to/mapper.py -mapper /your/path/to/mapper.py -file /your/path/to/reducer.py -reducer /your/path/to/reducer.py -input /user/your/path/transaction/input/retail.data -output /user/your/path/transaction/output2 -file /your/path/to/Ques1_strips
   ```

6. Fetch the output using the following command:
   ```
   hadoop fs -get /user/your/path/transaction/output2 /your/local/path/HW3_Stripes
   ```

   Check the output by running `cat part-00000 | head` in the output directory.

Please note that the code for Mapper.py, Reducer.py, and other files is not provided in the README. Make sure to refer to the actual code files for the complete implementation.
