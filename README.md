# CreditDefaults

## Intro and Setup:
Before running this script, be sure that at least Python 2 is installed (Python 3 preferred).
Also be sure to pip install the 'csv', 'json' and 'os' Python modules if you haven't already done so.

## Lib Folder:
Inside the lib folder is the out.arff file containing the initially discretized data we created from the initial dataset csv file.
This folder also contains the NonOutliers.csv this python script will create after it has filtered out all outlier data points.

The out_nonoutliers.arff file is the Weka arff file for the cleaned dataset resulting from this python script.
Finally, the clustering sub-directory contains the Weka model files for the default EM clustering algorithm results, as well as the numerous kMeans models we ran on the dataset. 
