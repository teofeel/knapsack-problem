from models.gene import Gene

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

    def copy(self):
        new_genes = [Gene(g.weight, g.value, g.added) for g in self.genes]
        return Chromosome(new_genes)
    