## CHIPS ATAC-seq Pipeline Description

The CHIPS pipeline is designed to perform robust quality control and reproducible processing of the chromatin profile sequencing data derived from ChIP-seq, DNase-seq, and ATAC-seq. The CHIPS pipeline includes procedures such as read alignment, peak calling, motif finding, and putative target prediction. The inputs to the pipeline are FASTQ/BAM format DNA sequence read files. The analysis process is split into three main components: read alignment, quality control and downstream analysis. The pipeline itself is encoded in the workflow language [Snakemake](https://snakemake.readthedocs.io/) and executed in a conda environment using the Google Cloud Compute Engine.

The main components of the CHIPs ATAC-seq pipline are:

* Read alignment
* Quality control:
    * Mapped reads
    * Sample contamination from other species.
    * Evolutionary conservation
    * Fraction of reads in peaks (FRIP) and PRC bottleneck (PBC) score
    * Overlapping with union Dnase Hypersensitivy Sites.
    * Number of high-quality peaks,
* Peak calling using [`MACS2`](https://github.com/macs3-project/MACS) and generating genome browser view [bigwig](https://genome.ucsc.edu/goldenPath/help/bigWig.html) file.
* Downstream analysis:
    * Peak annotation
    * putative target prediction using [Regulatory Potential](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-1934-6).
    * Motif enrichment using [`Homer`](http://homer.ucsd.edu/homer/motif/)


### workflow figure for ATAC-seq pipeline

![](https://raw.githubusercontent.com/CIMAC-CIDC/cidc-ngs-pipeline-api/master/cidc_ngs_pipeline_api/atacseq/imgs/atacseq.png)

## Versions of Tools and Reference Files Used in CHIPs

| Software         | Version | Source                | Notes               |
|------------------|---------|-----------------------|---------------------|
| snakemake        | 5.4.5   | bioconda              | Pipeline management |
| samtools         | 1.9     | bioconda              |                     | 
| python           | 3.6.8   | conda-forge           |                     |
| r                | 3.5.1   | conda-forge           |                     |
| numpy            | 1.16.3  | conda                 |                     |
| bwa              | 0.7.17  | bioconda              | Alignment           |
| picard           | 2.20.0  | bioconda              | Mark duplicates     |
| bedtools         | 2.27.1  | bioconda              |                     |
| gviz             | 1.26.4  | bioconda bioconductor |                     |
| seqtk            | 1.3     | bioconda              |                     |
| fastqc           | 0.11.8  | bioconda              |                     |
| ggplot2          | 3.1.1   | conda-forge r         |                     |
| reshape2         | 1.4.3   | conda-forge r         |                     |
| git              | 2.21.0  | conda-forge           |                     |
| perl             | 5.26.2  | conda-forge           |                     |
| homer            | 4.9.1   | bioconda              | Motif analysis      |
| weblogo          | 2.8.2   | bioconda              |                     |
| seqLogo          | 1.50.0  | bioconda bioconductor |                     |
| bedgraphtobigwig | 357     | bioconda ucsc         |                     |
| bedsort          | 357     | bioconda ucsc         |                     |
| seaborn          | 0.9.0   | conda-forge           |                     |
| r.utils          | 2.8.0   | conda-forge r         |                     |
| pybigwig         | 0.3.17  | bioconda              |                     |
| numpy            | 1.15.4  | conda                 |                     |
| cython           | 0.29.2  | conda                 |                     |
| jinja2           | 2.10.3  | conda                 |                     |
| macs2            | 2.2.4   | bioconda              | Peak calling        |
| fastp            | 0.20.1  | bioconda              | Adaptor trimming    |
