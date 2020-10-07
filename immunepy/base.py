class Cell:
    def __init__(self):
        self.name = "Base cell"
        self.location = None
        self.function = None

    def __repl__(self):
        return f'Cell(name={self.name})'


class HSC(Cell):
    def __init__(self):
        self.name = "Multipotential hematopoietic stem cell"
        self.location = "Bone marrow"
        self.function = "Stem cells that give rise to other blood cells"

    def lineage(self):
        """Print out lineage of cells."""
        pass
