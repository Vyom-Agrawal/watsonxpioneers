# GuardianEarth: AI for Biodiversity and Climate Resilience

## Project Overview

**GuardianEarth** is an AI-powered, one-stop platform that integrates global poaching data, biodiversity monitoring, satellite surveillance, legal compliance, and climate analytics to protect ecosystems and advance climate action. It leverages **IBM Watsonx.ai's Retrieval-Augmented Generation (RAG)** capabilities to synthesize diverse datasets—including NASA satellite imagery, wildlife trade databases, and human rights/legal reports—to provide actionable, rights-based risk assessments and compliance guidance.

## Key Features

- **Global Poaching Intelligence**  
  Aggregates real-time data from LEMIS, CITES, TRAFFIC, and media sources covering thousands of species and use types.

- **Satellite Surveillance**  
  Utilizes NASA's Harmonized Landsat Sentinel-2 (HLS-2) data to detect and monitor deforestation and habitat loss in poaching hotspots.

- **Citizen Science Integration**  
  Ingests and bias-corrects crowd-sourced reports from platforms like TARTLE.

- **AI-Driven Insights & Predictions**  
  Uses Watsonx.ai RAG pipeline to generate transparent, explainable risk assessments combining climate, biodiversity, and human rights/legal data.

- **Real-Time Alerts**  
  Sends SMS and app notifications to rangers, communities, and policymakers about imminent threats.

- **Community Empowerment**  
  Provides localized education modules and conservation tasks in multiple languages.

- **Policy & Compliance Auditing**  
  Audits conservation projects for compliance with OHCHR’s Free, Prior, and Informed Consent (FPIC) guidelines.

- **Legal Advice Integration**  
  Incorporates AI-powered legal advice APIs (e.g., Gemini, Thomson Reuters, Clio) to support climate legislation compliance and rights-based conservation.

## Judging Criteria Alignment

- **Creativity**  
  First solution to unite poaching, biodiversity, satellite, and human rights/legal data in a RAG-based AI platform.

- **Feasibility**  
  Built on IBM’s pre-trained geospatial models and scalable cloud infrastructure.

- **Design & Usability**  
  User-friendly dashboards, mobile alerts, and multilingual support.

- **Effectiveness**  
  Enables measurable reductions in poaching, habitat loss, and carbon emissions; supports SDGs 13 (Climate Action), 15 (Life on Land), and 16 (Peace, Justice).

## Legal Compliance Integration

### Supported Legal Features
1. **FPIC Compliance Checks**
   - Automatically audit conservation projects against OHCHR guidelines
2. **Climate Legislation Search**
   - Query national/international climate laws via Thomson Reuters API
3. **Document Automation**
   - Generate legal memos for carbon offset projects

### Setup Guide
1. Register for API keys:
   - [Gemini Legal API](https://gemini.legal)
   - [Thomson Reuters API](https://developers.thomsonreuters.com)
2. Add keys to `.env`

   - GEMINI_API_KEY="your_key"  
   - THOMSON_REUTERS_API_KEY="your_key"  

3. Use in code:

```python
from src.legal_advice import LegalCompliance

lc = LegalCompliance()
lc.generate_fpic_report({"location": "Congo Basin"})
