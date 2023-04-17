## Whole-exome sequencing (WES) analysis pipeline description

The CIDC whole-exome sequencing (WES) pipeline aims to identify and characterize key immunotherapeutic features of tumor samples.  WES implements the [Gene Analysis Toolkit](https://gatk.broadinstitute.org/hc/en-us) (GATK) best practices and identifies both somatic and germline variants using Sentieon's TNScope and Haplotyper algorithms, respectively.  Somatic variants are annotated using the Variant Effect Predictor software.  As recommended in [Chen YC, Seifuddin F, et al. 2021](https://www.biorxiv.org/content/10.1101/2021.02.18.431906v1.full), the pipeline uses an ensemble of three callers (CNVkit, Sequenza, and Facets) to characterize tumor copy number variation:  the overlap of the CNV segments is used to generate a high-confident consensus set.  WES estimates tumor purity using two different software packages, Sequenza and FACETS, and also infers tumor clonal populations using PyClone-VI. The pipeline characterizes tumor HLA type (both class I and class II alleles) using HLA-HD, xHLA, and Optitype.  WES also performs neoantigen prediction with pVACtools version 2.0.7 which incorporates netMHCpan 4.1 and netMHCpanII 4.0 as neoantigen callers and IEDB 3.1.1 to predict MHC peptide-MHC binding affinities and prioritize candidate epitopes.  WES estimates tumor tcell fraction using TCellExTRECT and tumor microsatellite instability using MSIsensor2.

### WES Workflow

![](https://raw.githubusercontent.com/CIMAC-CIDC/cidc-ngs-pipeline-api/master/cidc_ngs_pipeline_api/wes/imgs/wes.png)


## Versions of Tools and Reference Files Used in WES

| Reference/Software | Version | Source | Notes |
|--|--|--|--|
| Assembly | hg38 | GDC | modified to only include chr1-22,X,Y,M |
| Sentieon TNscope | sentieon-genomics-202010.01 | Sentieon | Somatic variant caller |
| Sentieon Haplotyper | sentieon-genomics-202010.01 | Sentieon | Germline variant caller |
| VEP  | 91.3  | Ensembl  | Variant annotation |
| CNVkit | 0.9.9 | bioconda | Copy number variation | 
| Sequenza | 2.1.2 | biobuilds  | Copy number variation; Tumor purity/ploidy |
| Sequenza-utils | 2.1.9999b0 | pip  | Copy number variation; Tumor purity/ploidy |
| Facets | 0.5.14  | bioconda | Copy number variation; Tumor purity/ploidy |
| PyClone-VI  | 0.1.1  | pip | Tumor clonality |
| HLA-HD | 1.4.0 | [website](https://www.genome.med.kyoto-u.ac.jp/HLA-HD/) | HLA typing |
| xHLA | commit 34221ea | [github](https://github.com/humanlongevity/HLA) | HLA typing |
| pVACtools  | 2.0.7 | pip | Neoantigen prediction |
| IEDB | 3.1.1 | [website](https://downloads.iedb.org/tools/mhci/3.1.1/)| Epitope database |
| TcellExTRECT | commit ec81143 | [github](https://github.com/McGranahanLab/TcellExTRECT)| Epitope database |
| MSIsensor2 | v0.1  | [github](https://github.com/niu-lab/msisensor2.git) |  Microsatellite instability |

---
## ExACdb assembly compatibility issue

### Issue:
The version of vcf2maf  (v1.6.18)  included in the CIDC WES pipeline uses ExACdb. CIDC WES uses the hg38 gene model. ExACdb is based on a hg19 reference, not hg38. Therefore some of the CIDC WES variants annotated by vcf2maf using ExACdb might not be accurate as the hg19/hg38 variant locations might be discrepant.

### CIDC Portal Files Affected (WES only):
The columns listed below in the output.twist.maf and output.twist.filtered.maf files.

### MAF fields affected in these files:
FILTER (though original FILTER flag is preserved; the ExAC_FILTER is added)

ExAC_FILTER, ExAC_AF_Adj, ExAC_AC_AN_Adj, ExAC_AC_AN, ExAC_AC_AN_AFR, ExAC_AC_AN_AMR, ExAC_AC_AN_EAS, ExAC_AC_AN_FIN, ExAC_AC_AN_NFE, ExAC_AC_AN_OTH, ExAC_AC_AN_SAS

Please see this [link](https://github.com/mskcc/vcf2maf/blob/47c4a18a15d5f93d4f3622615b3368448a74127d/docs/vep_maf_readme.txt) for more information about these fields.

---
