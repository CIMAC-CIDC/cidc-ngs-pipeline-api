#!/usr/bin/env python
"""Len Taing 2020 (TGBTG)"""

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
        self.long_description = file_tuple[1]
        self.filter_group = file_tuple[2]
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
    file_tuple[0] = file_tuple[0].replace(wildcard, s)
    return file_tuple
    
sample_files = [["analysis/align/{sample}/{sample}.sorted.dedup.bam",
                 "deduplicated bam: bam file with deduplicated reads",
                 "align/deduplicated_bam"], #ALIGN
                ["analysis/align/{sample}/{sample}.sorted.dedup.bam.bai",
                 "deduplicated bam index: bam index file for deduplicated bam",
                 "align/deduplicated_bam"],
                ["analysis/optitype/{sample}/{sample}_result.tsv",
                 "hla: MHC Class I results (using optitype)",
                 "HLA/optitype"], #HLA
                ["analysis/xhla/{sample}/report-{sample}-hla.json",
                 "hla: MHC Class I and II results (using xhla)",
                 "HLA/xhla"],
]

run_files = [["analysis/somatic/{run}/{run}_{caller}.output.vcf.gz",
              "somatic variants: vcf file of somatic variants",
              "somatic/vcf file"], #SOMATIC
             ["analysis/somatic/{run}/{run}_{caller}.filter.vcf.gz",
              "somatic variants: vcf file of filtered somatic variants",
              "somatic/filtered vcf file"],
             ["analysis/somatic/{run}/{run}_{caller}.filter.maf",
              "somatic variants: maf file of filtered somatic variants",
              "somatic/filtered maf file"],
             ["analysis/germline/{run}/{run}_vcfcompare.txt", #GERMLINE
              "somatic variants: overlap of somatic and germline variants",
              "somatic/variant overlap"],
             ["analysis/report2/somatic_variants/tumor_mutational_burden.tsv",
              "somatic variants: report file of tumor mutational burden in tumor and normal",
              "somatic/tmb report"],
             ["analysis/report2/neoantigens/HLA_results.tsv", #HLA
              "hla: report file of combined MHC class I and II results",
              "HLA/hla report"],
             ["analysis/neoantigen/{run}/combined/{run}.filtered.tsv", #NEOANTI
              "neaontigen: list of predicted neoantigens",
              "neoantigen/neoantigen list"],
             ["analysis/report2/copy_number/tumor_purity.tsv", #PURITY
              "tumor purity: tumor purity analysis results",
              "purity/purityresults"],
             ]

run_id_files = [Wesfile(r) for r in map(lambda x: evalWildcards(x, "{run}", "{run id}"), run_files)]
normal_files = [Wesfile(s) for s in map(lambda x: evalWildcards(x, "{sample}", "{normal cimac id}"), sample_files)]
tumor_files = [Wesfile(s) for s in map(lambda x: evalWildcards(x, "{sample}", "{tumor cimac id}"), sample_files)]

tmp = {'run id': run_id_files,
       "normal cimac id": normal_files,
       "tumor cimac id": tumor_files}

print(json.dumps(tmp, default=dumper, indent=4))

