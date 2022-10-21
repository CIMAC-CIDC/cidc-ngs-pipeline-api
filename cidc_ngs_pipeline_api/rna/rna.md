## RIMA (RNA-Seq IMmune Analysis) Pipeline Description

Tumor RNA-seq has become an important technique for molecular profiling and
immune characterization of tumors. RIMA (RNA-seq IMmune Analysis) performs
integrative computational modeling of tumor microenvironment from bulk tumor
RNA-seq data, which has the potential to offer essential insights to cancer
immunology and immune-oncology studies.
The pre-processing module includes four main procedures:
- Read mapping
- Quality control
- Gene quantification
- Batch effect removal

The downstream analysis includes seven modules:
- Differential gene expression 
- Immune infiltration estimation
- Immune repertoire estimation
- Gene fusion
- Immunotherapy response prediction
- HLA prediction
- Microbiome characterization

RIMA uses a conda virtual environment for software compiling and the python
Snakemake workflow management system for automatic batch processing.

### Workflow figure of RIMA pipeline

![](https://raw.githubusercontent.com/CIMAC-CIDC/cidc-ngs-pipeline-api/master/cidc_ngs_pipeline_api/rna/imgs/RIMA.png)

### Versions of Tools used in RIMA 

| Software         | Version | Source                | Notes                             |
|:-----------------|:--------|:----------------------|:----------------------------------|
| conda            | 4.8.3   | bioconda              | Environment Management            |
| Snakemake        | 5.5.4   | bioconda              | Pipeline Management               |
| python           | 3.6.8   | conda-forge           | Scripting  Language               |
| numpy            | 1.19.1  | conda-forge           | python library                    |
| perl             | 5.26.2  | conda-forge           | Scripting Language                |
| r                | 3.5.1   | conda-forge           | Scripting Language                |
| star             | 2.6.1   | bioconda              | Read Alignment                    |
| star-fusion      | 1.5.0   | bioconda              | Fusion Transcripts                |
| samtools         | 1.9     | bioconda              | Alignment Utility                 |
| salmon           | 1.3.0   | bioconda              | Gene Quantification               |
| picard           | 2.20.4  | bioconda              | Utility tool for aligned files    |
| bedtools         | 2.26.0  | bioconda              | Utility tool for aligned files    |
| bcftools         | 1.9     | bioconda              | BCF Manipulation                  |
| rseqc            | 3.0.1   | bioconda              | Quality Check                     |
| limma            | 3.42.0  | bioconductor          | Batch Removal                     |
| deseq2           | 1.26.0  | bioconductor          | Differential Expression Analysis  |
| MSISensor2       | 0.1     | git                   | Microsatellite Instability        |
| TRUST4           | 1.0.0   | git                   | Immune repertoire analysis        |
| arcasHLA         | 1.3.2   | git                   | HLA Typing                        |
| TIDEpy           | 1.3.6   | git                   | Immune response prediction        |         
| centrifuge       | 1.0.4   | bioconda              | Microbiome                        |
