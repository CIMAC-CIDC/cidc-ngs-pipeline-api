# CHIPs CIMAC-CIDC Pipeline Description

### Introduction

The CHIPS pipeline is designed to perform robust quality control and reproducible processing of the chromatin profile sequencing data derived from ChIP-seq, DNase-seq, and ATAC-seq. The CHIPS pipeline includes procedures such as read alignment, peak calling, motif finding, and putative target prediction — as discussed with other members of the CIMAC-CIDC Bioinformatics Working Group. The methods used in CHIPS will be re-evaluated to generate a specific result made by the comparison of different methods on pilot CHIPS data, a review of the literature, and occasional discussion. The pipeline will be adapted to incorporate better methods or new functions when needed. The inputs to the pipeline are FASTQ/BAM format DNA sequence read files, generated using sequencing protocols described in the Assays Section. The analysis process is split into three levels: Level 1 workflow, Level 2 workflow and Level 3 workflow. The pipeline itself is encoded in the workflow language Snakemake and executed in a conda environment using the Google Cloud Compute Engine.

CHIPS analysis is implemented across ten main procedures. 

* Read alignment
* Quality control
* Sample contamination 
* Copy number variation calling
* Peak calling
* Fraction of reads in peaks (FRIP) and PRC bottleneck (PBC) score
* CEAS (including intersect with union DHS)
* Gene target prediction 
* Motif enrichment
* Evolutionary conservation
