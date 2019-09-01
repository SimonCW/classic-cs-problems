from src.dna_search import string_to_gene


def test_string_to_gene_basic():
    gene_str = "AAACCCGGGAA"
    gene = string_to_gene(gene_str)
    assert len(gene) == 3
