#!/usr/bin/env python
"""Len Taing 2020 (TGBTG)"""

import sys
import json
from genson import SchemaBuilder


class Wesfile:
    """General wes file object that will handle outputing to appropriate
    json API format"""

    def __init__(self, file_tuple):
        """Given a file path, initializes this object to that path
        NOTE: filepath may include snakemake wildcards, e.g.
        analysis/germline/{run id}/{run id}_vcfcompare.txt"""
        # print(file_tuple)
        self.file_path_template = file_tuple[0]
        self.short_description = file_tuple[1]
        self.long_description = file_tuple[2]
        self.filter_group = file_tuple[3]
        if len(file_tuple) > 4:
            self.file_purpose = file_tuple[4]
        else:
            self.file_purpose = "Analysis view"

    def __str__(self):
        return self.__dict__.__str__()


def dumper(obj):
    # ref: https://www.semicolonworld.com/question/42934/how-to-make-a-class-json-serializable
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


def evalWildcards(file_tuple, wildcard, s):
    # file_tuple[0] = file_tuple[0].replace(wildcard, s)
    # Non-destructive replacement
    # print(file_tuple)
    ret = file_tuple.copy()
    ret[0] = ret[0].replace(wildcard, s)
    return ret


sample_files = [
    [
        "analysis/align/{sample}/{sample}.sorted.dedup.bam",
        "alignment: bam file with deduplicated reads",
        "Aligned reads were sorted and marked duplicates were removed using the Sentieon Dedup tool (https://support.sentieon.com/manual/usages/general/#dedup-algorithm)",
        "alignment",
        "Source view",
    ],  # ALIGN
    [
        "analysis/align/{sample}/{sample}.sorted.dedup.bam.bai",
        "alignment: bam index file for deduplicated bam",
        "Bam index file for deduplicated bam file generated by the Sentieon Dedup tool (https://support.sentieon.com/manual/usages/general/#dedup-algorithm)",
        "alignment",
        "Source view",
    ],
    [
        "analysis/optitype/{sample}/{sample}_result.tsv",
        "hla: MHC Class I results (using OptiType)",
        "Predicted MHC Class I alleles using the Optitype software (https://github.com/FRED-2/OptiType).  Chromosome 6 reads from the deduplicated bam file were extracted and fed into the Optitype prediction algorithm.",
        "HLA",
    ],  # HLA
    [
        "analysis/xhla/{sample}/report-{sample}-hla.json",
        "hla: MHC Class I and II results (using xhla)",
        "Predicted MHC Class II and II results using the xHLA software(https://github.com/humanlongevity/HLA).  Chromosome 6 reads from the deduplicated bam file were extracted and fed into the xHLA prediction algorithm.",
        "HLA",
    ],
    [
        "analysis/metrics/{sample}/{sample}_coverage_metrics.txt",
        "coverage: global coverage file",
        "Genome wide coverage file generated using the Sentieon CoverageMetrics algorithm (https://support.sentieon.com/manual/usages/general/#coveragemetrics-algorithm) with a coverage threshold (cov_thresh) set to 50.",
        "coverage",
    ],  # COVERAGE
    [
        "analysis/metrics/{sample}/{sample}_target_metrics.txt",
        "coverage: target region coverage file",
        "Targeted exome regions coverage file using the Sentieon CoverageMetrics algorithm (https://support.sentieon.com/manual/usages/general/#coveragemetrics-algorithm) with a coverage threshold (cov_thresh) set to 50.",
        "coverage",
    ],
    [
        "analysis/metrics/{sample}/{sample}_coverage_metrics.sample_summary.txt",
        "coverage: global coverage summary file",
        "Genome wide coverage summary file generated by the Sentieon CoverageMetrics algorithm (https://support.sentieon.com/manual/usages/general/#coveragemetrics-algorithm).",
        "coverage",
    ],
    [
        "analysis/germline/{sample}/{sample}_haplotyper.targets.vcf.gz",
        "germline: vcf of haplotype variants in targeted regions",
        "Haplotype variants within targeted capture regions using Sentieon Haplotyper algorithm (https://support.sentieon.com/manual/usages/general/#haplotyper-algorithm)",
        "germline",
    ],  # Germline
]

run_files = [
    [
        "analysis/somatic/{run}/{run}_{caller}.output.vcf.gz",
        "somatic variants: vcf file of somatic variants",
        """VCF file of somatic variants using one of the following the Sentieon somatic callers {tnscope (default), tnhaplotyper2, tnsnv}.

TNscope algorithm- https://support.sentieon.com/manual/usages/general/#tnscope-algorithm
TNhaplotyper2- https://support.sentieon.com/manual/usages/general/#tnhaplotyper2-algorithm
TNsnv - https://support.sentieon.com/manual/usages/general/#tnsnv-algorithm""",
        "somatic",
    ],  # SOMATIC
    [
        "analysis/somatic/{run}/{run}_{caller}.output.maf",
        "somatic variants: maf file of somatic variants",
        "MAF file of VEP annotated variants using vcf2maf tool (https://github.com/mskcc/vcf2maf).  The vep annotated vcf (output.vcf.gz) file was used as the input for vcf2maf.",
        "somatic",
    ],
    [
        "analysis/somatic/{run}/{run}_{caller}.filter.vcf.gz",
        "somatic variants: vcf file of filtered somatic variants",
        "VCF file of filtered somatic variants.  With the output.vcf file as input, the vcftools software was used with parameter --remove-filtered-all to remove any variants whose FILTER column is anything other than PASS.  see http://vcftools.sourceforge.net/man_latest.html",
        "somatic",
    ],
    [
        "analysis/somatic/{run}/{run}_{caller}.filter.maf",
        "somatic variants: maf file of filtered somatic variants",
        "MAF file of VEP annotated filtered variants using vcf2maf tool (https://github.com/mskcc/vcf2maf).  The filtered vep annotated vcf file (filter.vep.vcf) file was used as input for vcf2maf.",
        "somatic",
    ],
    [
        "analysis/somatic/{run}/{run}_{caller}.filter.exons.vcf.gz",
        "somatic variants: vcf file of filtered somatic variants from center target regions",
        "VCF file of filtered somatic variants from center target regions using bcftools (http://samtools.github.io/bcftools/bcftools.html).",
        "somatic",
    ],
    # Drop vcfcompare.txt?? b/c we have tmb.tsv below
    [
        "analysis/germline/{run}/{run}_vcfcompare.txt",  # GERMLINE
        "somatic variants: overlap of somatic and germline variants",
        "VCFtool's vcf-compare (http://vcftools.sourceforge.net/perl_module.html#vcf-compare) is used to compare somatic and germline variants.  The file shows the number of common variants, somatic only, and germline only variants.",
        "somatic",
    ],
    [
        "analysis/report/somatic_variants/07_tumor_mutational_burden.tsv",
        "somatic variants: report file of tumor mutational burden in tumor and normal",
        "This file derived from the somatic and germline variants comparison results generated by vcf-compare (http://vcftools.sourceforge.net/perl_module.html#vcf-compare) and is formatted to be human readable.  The file reports the number of somatic/tumor only variants, germline/normal only variants, the number of shared variants, and the percent overlap (using the total number of somatic variants as the denominator).",
        "somatic",
    ],
    [
        "analysis/report/neoantigens/01_HLA_results.tsv",  # HLA
        "hla: report file of combined MHC class I and II results",
        "This file reports the MHC class I and II results.  The class I alleles are derived from the OptiType results and the class II alleles come from the xHLA results. ",
        "HLA",
    ],
    [
        "analysis/neoantigen/{run}/combined/{run}.filtered.tsv",  # NEOANTI
        "neaontigen: list of predicted neoantigens",
        "The combined MHC class I and II predicted neoantigens using the pVACseq software.  The column definitions are given here (ref: https://pvactools.readthedocs.io/en/latest/pvacseq/output_files.html)",
        "neoantigen",
    ],
    [
        "analysis/purity/{run}/{run}.optimalpurityvalue.txt",  # PURITY
        "tumor purity: tumor purity analysis results",
        "Tumor purity calculations using the FACETS software (https://github.com/mskcc/facets)..",
        "purity",
    ],
    [
        "analysis/clonality/{run}/{run}_pyclone.tsv",  # CLONALITY
        "tumor clonality: PyClone input file generated by sequenza library (https://cran.r-project.org/web/packages/sequenza/index.html)",
        "Input file generated for PyClone analysis.  Sequenza was used to generate the expected file format (https://github.com/Roth-Lab/pyclone#input-format).",
        "clonality",
    ],
    [
        "analysis/clonality/{run}/{run}_table.tsv",
        "tumor clonality: tumor clonality analysis results",
        "Tumor clonality results using PyClone software (https://github.com/Roth-Lab/pyclone)..",
        "clonality",
    ],
    [
        "analysis/copynumber/{run}/{run}_cnvcalls.txt",  # CNV
        "copynumber: copynumber analysis results",
        "Copy number variation analysis results using Sentieon CNV algorithm (https://support.sentieon.com/appnotes/cnv/)",
        "copynumber",
    ],
    [
        "analysis/copynumber/{run}/{run}_cnvcalls.txt.tn.tsv",
        "copynumber: copynumber analysis results",
        "Segmented copy number variation file using Sentieon CNV algorithm (https://support.sentieon.com/appnotes/cnv/)",
        "copynumber",
    ],
    [
        "analysis/msisensor2/{run}/{run}_msisensor.txt",  # MSISENOR2
        "msisensor2: microsatellite instability calculation",
        "Microsatellite instability calculation using msisensor2 (https://github.com/niu-lab/msisensor2)",
        "msisensor2",
    ],
    [
        "analysis/report.tar.gz",  # REPORT
        "wes report: wes summary html report",
        "This is a gzipped file of the report directory, which contains the report.html file.  After unzipping the file, the user can load report/report.html into any browser to view the WES Summary Report.  The report contains run information (i.e. wes software version used to run the analysis as well as the software version of the major tools) as well as summarizations of sample quality, copy number variation, somatic variants, and HLA-type/neoantigen predictions.",
        "report",
    ],
    [
        "analysis/report/wes_meta/02_wes_run_version.tsv",
        "wes pipeline version- INTERNAL ONLY- for reproducibility",
        "wes pipeline version- INTERNAL ONLY- for reproducibility",
        "report",
        "Miscellaneous",
    ],
    [
        "analysis/report/config.yaml",
        "wes pipeline config file- INTERNAL ONLY- for reproducibility",
        "wes pipeline config file- INTERNAL ONLY- for reproducibility",
        "report",
        "Miscellaneous",
    ],
    [
        "analysis/report/metasheet.csv",
        "wes pipeline metasheet file- INTERNAL ONLY- for reproducibility",
        "wes pipeline metasheet file- INTERNAL ONLY- for reproducibility",
        "report",
        "Miscellaneous",
    ],
    [
        "analysis/report/json/{run}.wes.json",
        "wes sample json for cohort report generation-INTERNAL ONLY",
        "wes sample json for cohort report generation-INTERNAL ONLY",
        "report",
        "Miscellaneous",
    ],
]

run_id_files = [
    r for r in map(lambda x: evalWildcards(x, "{run}", "{run id}"), run_files)
]
run_id_files = [
    Wesfile(r)
    for r in map(lambda x: evalWildcards(x, "{caller}", "tnscope"), run_id_files)
]

normal_files = [
    Wesfile(s)
    for s in map(
        lambda x: evalWildcards(x, "{sample}", "{normal cimac id}"), sample_files
    )
]
tumor_files = [
    Wesfile(s)
    for s in map(
        lambda x: evalWildcards(x, "{sample}", "{tumor cimac id}"), sample_files
    )
]

tmp = {
    "run id": run_id_files,
    "normal cimac id": normal_files,
    "tumor cimac id": tumor_files,
}

# print(json.dumps(tmp, default=dumper, indent=4))
json.dump(tmp, open("wes_output_API.json", "w"), default=dumper, indent=4)
