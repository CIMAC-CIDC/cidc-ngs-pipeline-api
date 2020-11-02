# TCR-seq CIMAC-CIDC Report Description

### Summary 

An in-browser immune repertoire report, relying on VisualizIRR (Visualized Immune Repertoire Report), is used make immune repertoire analysis results simple to navigate and understand for the end user on their local machine or on a server.
The report contains analysis on the cohort and sample level in order to inform the end user of CDR3 distribution, top clonotypes, and V/J-gene usage.
Additional information related to diversity and clonality is also included in an intracohort analysis module and is displayed on a boxplot that may be split by meta-information, when it is available.
When multiple chains are available in the dataset, they are seperated.
Information in the report is displayed mostly through interactive plots which may be exported at a higher resolution.

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

### Information in Report

* Cohort and sample level 
    * Segment Usage
        * V gene and J gene usage
        * Combined V and J gene usage
    * CDR3 Info
        * CDR3 length distribution
        * Top clonotypes
* Intracohort Analysis & Information Table
    * Raw Diversity 
    * Entropy, 1/Entropy, Normalized Entropy
    * Gini Coefficient
    * Gini-Simpson Index
    * Inverse Simpson Index
    * Chao1 Index
    * Clonal Proportionality Information
    * Average CDR3 Length
    * Unique CDR3 Count
