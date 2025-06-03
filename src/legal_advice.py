import os
import requests

class LegalCompliance:
    def __init__(self):
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.thomson_key = os.getenv("THOMSON_REUTERS_API_KEY")
    
    def get_climate_laws(self, country: str):
        """Retrieve climate legislation using Thomson Reuters API"""
        url = "https://api.thomsonreuters.com/climate-laws"
        headers = {"Authorization": f"Bearer {self.thomson_key}"}
        params = {"jurisdiction": country}
        return requests.get(url, headers=headers, params=params).json()
    
    def generate_fpic_report(self, project_data: dict):
        """Generate FPIC compliance report using Gemini API"""
        url = "https://api.gemini.legal/v1/analyze"
        headers = {"Authorization": f"Bearer {self.gemini_key}"}
        payload = {
            "template": "fpic_checklist",
            "data": project_data
        }
        return requests.post(url, json=payload, headers=headers).json()

# Usage example:
# compliance = LegalCompliance()
# print(compliance.get_climate_laws("Kenya"))
