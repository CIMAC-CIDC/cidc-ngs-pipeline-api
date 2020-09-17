#!/usr/bin/env python
"""Len Taing 2020 (TGBTG)"""

import sys
import json
from genson import SchemaBuilder

class Wesfile():
    """General wes file object that will handle outputing to appropriate
    json API format"""
    def __init__(self, file_tuple):
        """Given a file path, initializes this object to that path
        NOTE: filepath may include snakemake wildcards, e.g.
        analysis/germline/{run id}/{run id}_vcfcompare.txt"""
        #print(file_tuple)
        self.file_path_template = file_tuple[0]
        self.short_description = file_tuple[1]
        self.long_description = file_tuple[2]
        self.filter_group = file_tuple[3]
        if len(file_tuple) > 4:
            self.file_purpose = file_tuple[4]
        else:
            self.file_purpose = "Analysis file"
        
    def __str__(self):
        return self.__dict__.__str__()
    
def dumper(obj):
    #ref: https://www.semicolonworld.com/question/42934/how-to-make-a-class-json-serializable
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

def evalWildcards(file_tuple, wildcard, s):
    #file_tuple[0] = file_tuple[0].replace(wildcard, s)
    #Non-destructive replacement
    #print(file_tuple)
    ret = file_tuple.copy()
    ret[0] = ret[0].replace(wildcard, s)
    return ret
    
sample_files = [["analysis/align/{sample}/{sample}.sorted.dedup.bam",
                 "alignment: bam file with deduplicated reads",
                 "Aligned reads were sorted and marked duplicates were removed",
                 "alignment", "Source file"], #ALIGN
                ["analysis/align/{sample}/{sample}.sorted.dedup.bam.bai",
                 "alignment: bam index file for deduplicated bam",
                 "Bam index file for deduplicated bam file",
                 "alignment", "Source file"],
                ["analysis/optitype/{sample}/{sample}_result.tsv",
                 "hla: MHC Class I results (using OptiType)",
                 "Predicted MHC Class I alleles using the Optitype software",
                 "HLA"], #HLA
                ["analysis/xhla/{sample}/report-{sample}-hla.json",
                 "hla: MHC Class I and II results (using xhla)",
                 "Predicted MHC Class II and II results using the xHLA software",
                 "HLA"],
                ["analysis/metrics/{sample}/{sample}_coverage_metrics.txt",
                 "coverage: global coverage file",
                 "Genome wide read depth file",
                 "coverage"], #COVERAGE
                ["analysis/metrics/{sample}/{sample}_target_metrics.txt",
                 "coverage: target region coverage file",
                 "Targeted exome regions read depth file",
                 "coverage"],
                ["analysis/metrics/{sample}/{sample}_coverage_metrics.sample_summary.txt",
                 "coverage: global coverage summary file",
                 "Global coverage summary file",
                 "coverage"],

]

run_files = [["analysis/somatic/{run}/{run}_{caller}.output.vcf.gz",
              "somatic variants: vcf file of somatic variants",
              "VCF file of somatic variants",
              "somatic"], #SOMATIC
             ["analysis/somatic/{run}/{run}_{caller}.output.maf",
              "somatic variants: maf file of somatic variants",
              "MAF file of VEP annotated variants",
              "somatic"],
             ["analysis/somatic/{run}/{run}_{caller}.filter.vcf.gz",
              "somatic variants: vcf file of filtered somatic variants",
              "VCF file of filtered somatic variants",
              "somatic"],
             ["analysis/somatic/{run}/{run}_{caller}.filter.maf",
              "somatic variants: maf file of filtered somatic variants",
              "MAF file of filtered variants annotated by VEP",
              "somatic"],
             ["analysis/somatic/{run}/{run}_{caller}.filter.exons.{center}.vcf.gz",
              "somatic variants: vcf file of filtered somatic variants from center target regions",
              "VCF file of filtered somatic variants from center target regions ",
              "somatic"],
             #Drop vcfcompare.txt?? b/c we have tmb.tsv below
             ["analysis/germline/{run}/{run}_vcfcompare.txt", #GERMLINE
              "somatic variants: overlap of somatic and germline variants",
              "VCFtools is used to compare somatic and germline variants.  The file shows the number of common variants, somatic only, and germline only variants.",
              "somatic"],
             ["analysis/report/somatic_variants/07_tumor_mutational_burden.tsv",
              "somatic variants: report file of tumor mutational burden in tumor and normal",
              "This file derived from the VCFtools somatic and germline variants comparison result and is displayed in a readable manner.  The file reports the number of somatic/tumor only variants, germline/normal only variants, the number of shared variants, and the percent overlap (using the total number of somatic variants as the denominator).",
              "somatic"],
             ["analysis/report/neoantigens/01_HLA_results.tsv", #HLA
              "hla: report file of combined MHC class I and II results",
              "This file reports the MHC class I and II results.  The class I alleles are derived from the OptiType results and the class II alleles come from the xHLA results. ",
              "HLA"],
             ["analysis/neoantigen/{run}/combined/{run}.filtered.tsv", #NEOANTI
              "neaontigen: list of predicted neoantigens",
              "The combined MHC class I and II prediected neoantigens using the pVACseq software.  The column definitions are given here (ref: https://pvactools.readthedocs.io/en/latest/pvacseq/output_files.html)",
              "neoantigen"],
             ["analysis/purity/{run}/{run}.optimalpurityvalue.txt", #PURITY
              "tumor purity: tumor purity analysis results",
              "Tumor purity calculations using the FACETS software.",
              "purity"],
             ["analysis/clonality/{run}/{run}_pyclone.tsv", #CLONALITY
              "tumor clonality: tumor clonality analysis results",
              "Tumor clonality results using PyClone software.",
              "clonality"],
             ["analysis/copynumber/{run}/{run}_cnvcalls.txt", #CNV
              "copynumber: copynumber analysis results",
              "Copy number variation analysis results using Sentieon CNV algorithm",
              "copynumber"],
             ["analysis/copynumber/{run}/{run}_cnvcalls.txt.tn.tsv",
              "copynumber: copynumber analysis results",
              "Segmented copy number variation file using Sentieon CNV algorithm",
              "copynumber"],
             ["analysis/report.tar.gz", #REPORT
              "wes report: wes summary html report",
              "WES summary report",
              "report"],
             ["analysis/report/wes_meta/02_wes_run_version.tsv",
              "wes pipeline version",
              "wes pipeline version",
              "report"],
             ["analysis/report/config.yaml",
              "wes pipeline config file",
              "wes pipeline config file",
              "report"],
             ["analysis/report/metasheet.csv",
              "wes pipeline metasheet file",
              "wes pipeline metasheet file",
              "report"],
             ]

run_id_files = [Wesfile(r) for r in map(lambda x: evalWildcards(x, "{run}", "{run id}"), run_files)]
normal_files = [Wesfile(s) for s in map(lambda x: evalWildcards(x, "{sample}", "{normal cimac id}"), sample_files)]
tumor_files = [Wesfile(s) for s in map(lambda x: evalWildcards(x, "{sample}", "{tumor cimac id}"), sample_files)]

tmp = {'run id': run_id_files,
       "normal cimac id": normal_files,
       "tumor cimac id": tumor_files}

print(json.dumps(tmp, default=dumper, indent=4))

