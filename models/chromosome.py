class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.calculate_weight()

    def add_gene(self, gene):
        self.genes.append(gene)
        self.weight += gene.weight

    def calculate_weight(self):
        self.weight = 0
        for g in self.genes:
            self.weight += g.weight

    