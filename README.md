# BigData Workshop - BITS Pilani, Dubai Campus 

This repository contains code and support files for the BigData Workshop. The workshop materials include:

## Program Files
1. `activity.py`: This Python file contains the implementation of a MapReduce job and additional analysis on word counts. It analyzes documents provided in the support files.
2. `activity.ipynb`: This Jupyter Notebook contains the same exercise as `activity.py`, providing a hands-on approach to the workshop material. It serves as an alternative for those who prefer a notebook environment.

## Support Files

The workshop includes three support files containing text data for analysis:

1. `text_100k. txt`: A text file containing a large dataset for analysis.
2. `text_30k. txt`: A text file containing a medium-sized dataset for analysis.
3. `text_10k. txt`: A text file containing a small dataset for analysis.

Feel free to use any text corpus of your choice for the activity

## Running the Code

To run the Jupyter Notebook `activity.ipynb`, you can upload it to Google Colab or have Jupyter Notebook installed along with Python. Launch Jupyter Notebook and open the notebook file. Follow the instructions within the notebook to execute the code cells and perform the analysis.

To run the code provided in `activity.py`, ensure you have Python installed on your system. Then, execute the script using a Python interpreter. The script will perform a MapReduce job on the text data provided in the support files and analyze the word counts.

Clone this repository to your local machine:

``` bash
git clone https://github.com/your-username/BigData-Bits-University-Workshop.git
cd BigData-Bits-University-Workshop
```

Run the MapReduce job using the provided Python script:
``` bash
python activity.py
```

## Workshop Results
After running the MapReduce job, you'll obtain insights into the word frequencies in the provided text files. The program displays the most common word, the least common word, and the average word frequency. Feel free to experiment with different text files to observe how the MapReduce job performs on varying datasets.


Runtimes
For your convenience, I've included runtime information for different text files in the `activity.py` file. You can assess the performance of the MapReduce job on each dataset and compare the results.

Feel free to reach out if you have any questions or need further clarification. Happy coding!