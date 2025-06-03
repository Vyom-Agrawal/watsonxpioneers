from src.legal_advice import LegalCompliance

class GuardianRAG:
    def __init__(self):
        self.legal = LegalCompliance()
    
    def analyze_project(self, coordinates):
        laws = self.legal.get_climate_laws("Kenya")
        fpic_report = self.legal.generate_fpic_report({
            "coordinates": coordinates,
            "community_size": 1500
        })
        return {**laws, **fpic_report}
      
