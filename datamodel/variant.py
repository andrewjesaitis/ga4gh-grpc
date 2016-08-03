import os

import pysam

import ga4gh

VARIANT_FILE = os.path.abspath("data/release/ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz")

def getPysamVariants(reference, chromosome, start, end):
    vcf = pysam.VariantFile(VARIANT_FILE)
    return vcf.fetch(chromosome, start, end)


