GS = 'Gold standard'
SUPERKINGDOM = 'superkingdom'
PHYLUM = 'phylum'
CLASS = 'class'
ORDER = 'order'
FAMILY = 'family'
GENUS = 'genus'
SPECIES = 'species'
STRAIN = 'strain'
PHYLUM_SPECIES = [PHYLUM, CLASS, ORDER, FAMILY, GENUS, SPECIES]
ALL_RANKS = [SUPERKINGDOM, PHYLUM, CLASS, ORDER, FAMILY, GENUS, SPECIES, STRAIN]

UNIFRAC = 'Weighted Unifrac error'
UNW_UNIFRAC = 'Unweighted Unifrac error'
L1NORM = 'L1 norm error'
PRECISION = 'Purity (precision)'
RECALL = 'Completeness (recall)'
F1_SCORE = 'F1 score'
TP = "True positives"
FP = 'False positives'
FN = "False negatives"
OTUS = "Taxon counts"
JACCARD = "Jaccard index"
SHANNON_DIVERSITY = 'Shannon diversity'
SHANNON_EQUIT = 'Shannon equitability'
BRAY_CURTIS = 'Bray-Curtis distance'
ALL_METRICS = [UNIFRAC, UNW_UNIFRAC, L1NORM, PRECISION, RECALL, F1_SCORE, TP, FP, FN, JACCARD, SHANNON_DIVERSITY, SHANNON_EQUIT, BRAY_CURTIS]
