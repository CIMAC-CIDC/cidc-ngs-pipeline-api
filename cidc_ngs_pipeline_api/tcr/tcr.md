# TCR-seq CIMAC-CIDC Report Description

### Summary 

An in-browser immune repertoire report, relying on VisualizIRR (Visualized Immune Repertoire Report), is used make immune repertoire analysis results simple to navigate and understand for the end user on their local machine or on a server.
The report contains analysis on the cohort and sample level in order to inform the end user of CDR3 distribution, top clonotypes, and V/J-gene usage.
Additional information related to diversity and clonality is also included in an intracohort analysis module and is displayed on a boxplot that may be split by meta-information, when it is available.
When multiple chains are available in the dataset, they are seperated.
Information in the report is displayed mostly through interactive plots which may be exported at a higher resolution.

### Decompressing the report file

The report can be downloaded from the CIDC portal in tar.gz compressed format.  On a Mac, one can simply double-click on the <report_name>.tar.gz file to decompress the file.  The file can also be decompressed in a terminal window using the bash command tar:

```
tar -xvzf <report_name>tar.gz
```

On a Windows-based system, a third-party software such as Winzip can be used to decompress the file.

### Viewing Report on a Local Machine

For security purposes, newer browsers can have problems loading local files normally in an HTML page.
If you can't view the the display locally by simply opening the html in a browser, you can perform the following in your terminal to set up a simple server and view the report:
```
cd <VisualizIRR_directory>
```
Python 2:
```
python -m SimpleHTTPServer & python -m webbrowser -n "http://0.0.0.0:8000"
```
Python 3:
```
python3 -m http.server & python3 -m webbrowser -n "http://0.0.0.0:8000"
```

The report is viewable at http://0.0.0.0:8000, which should pop up automatically.

### TCR-seq Workflow

![](https://raw.githubusercontent.com/CIMAC-CIDC/cidc-ngs-pipeline-api/master/cidc_ngs_pipeline_api/tcr/imgs/TCRseq.png)

### Adding metadata to the report
**meta.csv** is required for intracohort analysis and is the only component of the final report that needs to be manually composed by the end-user.

**meta.csv** can be found within the report folder in the **data** subdirectory.

**meta.csv** should be a csv with the first column including sample names and remaining columns for different conditions.
There are a few ways to enter your meta information. 
    
1. In order to have ordered sample condition groups, denote the categorical label of those groups in the header using '|' as the separator and use the corresponding numbers in the sample rows, starting with 0 for the first label (as demonstrated in Timepoint and Condition 1).
2. You can also use the labels in the metasheet and not denote them in the header (as demonstrated in Age and Condition 2).
3. Meta-data should be converted to categorical bins if it isn't categorical already (as demonstrated in Age)
4. In order to set up paired samples analysis, two columns must be in the meta.csv -- 'Timepoint' and 'VisGroup'. 'Timepoint' should contain ordered labels as described above. The column named 'VisGroup' indicates which samples should be paired. (as demonstrated in the meta.csv sample below, SampleName1 and SampleName3 are paired. SampleName1 is a sample taken at Baseline.  SampleName3 is a sample taken at Cycle 2.)  Therefore, patient samples from different timepoints can be paired.

meta.csv template:
```
sample,Timepoint|Baseline|Cycle 1|Cycle 2,Age,Condition 1|Group 0|Group 1|Group 2,Condition 2,VisGroup
SampleName0,1,20-29,0,Aa,0
SampleName1,0,40-49,2,Bb,1
SampleName2,1,10-19,1,Cc,2
SampleName3,2,40-49,2,Bb,1
```

### Video Tutorial
The following video describes decompressing and opening the report as well as how to modify the meta.csv file.

[![Watch the video](http://img.youtube.com/vi/vmDwjSrei0c/0.jpg)](https://www.youtube.com/watch?v=vmDwjSrei0c)

### Information in Report

* Cohort and sample level 
    * Segment Usage
        * V gene and J gene usage
        * Combined V and J gene usage
    * CDR3 Info
        * CDR3 length distribution
        * Top clonotypes
* Intracohort Analysis & Information Table
    * Clonotypes Per Kilo-reads (CPK)
    * Raw Diversity 
    * Entropy, 1/Entropy, Normalized Entropy
    * Gini Coefficient
    * Gini-Simpson Index
    * Inverse Simpson Index
    * Chao1 Index
    * Clonal Proportionality Information
    * Average CDR3 Length
    * Unique CDR3 Count
