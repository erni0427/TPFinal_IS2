class Species:
    """Model of a seagrass species."""
    
    def __init__(self, name, growth_rate, mortality_rate, competitiveness):
        self.name = name
        self.growth_rate = growth_rate
        self.mortality_rate = mortality_rate
        self.competitiveness = competitiveness

class SpeciesFactory:
    """Factory for creating species based on their names."""
    
    @staticmethod
    def create_species(name):
        species_map = {
            "Posidonia oceanica": Species(name, 0.08, 0.03, 2),
            "Cymodocea nodosa": Species(name, 0.05, 0.02, 3),
            "Halophila stipulacea": Species(name, 0.12, 0.04, 10)
        }
        if name not in species_map:
            raise ValueError(f"Species '{name}' not recognized.")
        return species_map[name]