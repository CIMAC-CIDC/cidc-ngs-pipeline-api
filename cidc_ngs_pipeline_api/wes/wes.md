## WES (Whole-exome sequencing) pipeline description

The whole-exome sequencing (WES) [Snakemake](https://snakemake.readthedocs.io/) pipeline is based on [`GATK`](https://gatk.broadinstitute.org/hc/en-us) (Gene Analysis Toolkit) best practices. Paired tumor and normal whole-exome sequencing files (either as fastqs or unmapped bams) are aligned by [`BWA-mem`](https://github.com/lh3/bwa) to a modified GDC GRCh38 reference (containing only chromosomes 1-22,X,Y,M) and is followed by duplicate marking, base recalibration, and realignment. Sequence quality metrics are measured by [`Sentieon`](https://www.sentieon.com/products/) Quality metrics, which is similar to `FASTQC`. The  germline variants are called using Sentieon [`Haplotyper`](https://support.sentieon.com/manual/usages/general/#haplotyper-algorithm). Somatic variants are called by [`TNScope`](https://support.sentieon.com/manual/usages/general/#tnscope-algorithm) (also from Sentieon) and are annotated by [`VEP`](https://uswest.ensembl.org/info/docs/tools/vep/index.html). Tumor purity and ploidy are computed by [`FACETS`](https://github.com/mskcc/facets) while a combination of [`Sequenza`](https://cran.r-project.org/web/packages/sequenza/vignettes/sequenza.html) and [`PyClone`](https://github.com/Roth-Lab/pyclone) is used to generate the tumor clonal distribution. HLA-alleles are predicted through [`Optitype`](https://github.com/FRED-2/OptiType) and [`xHLA`](https://github.com/humanlongevity/HLA) for classI and classII alleles respectively.  Neoantigens are calculated using [`PVACseq`](https://github.com/griffithlab/pVAC-Seq).

### WES Workflow

![](https://raw.githubusercontent.com/CIMAC-CIDC/cidc-ngs-pipeline-api/master/cidc_ngs_pipeline_api/wes/imgs/wes.png)


## Versions of Tools and Reference Files Used in WES

| Referece/Software   | Version                     | Source   | Notes                                |
|------------|-----------------------------|----------|-------------------------------------|
| Assembly   | hg38 | GDC | chr1-22,X,Y,M |
| Sentieon   | sentieon-genomics-201808.05 | Sentieon | concordant with GATK best practice  |
| BWA        | sentieon-genomics-201808.05 (bwa 0.7.15-r1140) | Sentieon | Read aligner  |
| tnscope    | sentieon-genomics-201808.05 | Sentieon | Somatic caller                      |
| VEP        | 91.3                        | Ensembl  | Variant annotation                  |
| Facets     | 0.5.14                      | bioconda | Tumor purity/ploidy                 |
| Sequenza   | 2.1.9999b0                  | pip      | Tumor clonality                     |
| PyClone    | 0.13.1                      | bioconda | Tumor clonality                     |
| Optitype   | 1.3.2                       | bioconda | Class I HLA caller                  |
| xHLA       | 34221ea                     | [github](https://github.com/humanlongevity/HLA) | Class II HLA caller                 |
| PVACseq    | 1.3.7                       | bioconda | Neoantigen prediction               |
| MSIsensor2 | v0.1                        | [github](https://github.com/niu-lab/msisensor2.git)         |        microsatellite   instability |
| VCFtools   | 0.1.16                      | bioconda | VCF manipulation                    |
| BCFtools   | 1.9                         | bioconda | BCF manipulation                    |
| Snakemake  | 5.4.5                       | bioconda | Pipeline management                 |
