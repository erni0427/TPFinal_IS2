import logging

class Climate:
    """Encapsulates the effects of climate on the simulation."""
    
    def __init__(self, temp_increase, salinity_increase):
        self.temp_increase = temp_increase
        self.salinity_increase = salinity_increase
        logging.info(f"Climate initialized: Temp increase {temp_increase}, Salinity increase {salinity_increase}")