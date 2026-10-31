#!/usr/bin/env python3
"""
World Wide Law Global Legal Data Hunter
Framework for Scraping and Normalizing Multi-Jurisdictional Legal Data (110+ Countries)
"""

import sys
import os
import json
import hashlib
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

JURISDICTION_REGISTRY = {
    "CU": {
        "country": "Cuba",
        "official_gazette_url": "https://www.gacetaoficial.gob.cu",
        "key_statutes": ["Ley 851 (Nationalization)", "Ley 890 (Expropriation of Industrial Enterprises)"],
        "target_archives": ["Archivo Nacional de Cuba", "Registro Mercantil Central"]
    },
    "PA": {
        "country": "Panama",
        "mercantile_registry_url": "https://www.rp.gob.pa",
        "key_statutes": ["Código de Comercio de Panamá", "Ley de Sociedades Anónimas (Ley 32 de 1927)"],
        "target_archives": ["Registro Público de Panamá", "Tribunal Marítimo de Panamá"]
    },
    "CA": {
        "country": "Canada",
        "legislation_url": "https://laws-lois.justice.gc.ca",
        "key_statutes": ["Federal Courts Act, R.S.C. 1985, c. F-7", "State Immunity Act, R.S.C. 1985, c. S-18"],
        "target_archives": ["Federal Court of Canada Registry (Montreal / Halifax)"]
    },
    "ES": {
        "country": "Spain",
        "official_bulletin_url": "https://www.boe.es",
        "key_statutes": ["Ley Orgánica 16/2015 sobre privilegios e inmunidades de los Estados extranjeros", "Ley de Enjuiciamiento Civil"],
        "target_archives": ["Boletín Oficial del Estado", "Audiencia Nacional"]
    },
    "NL": {
        "country": "Netherlands",
        "legislation_url": "https://wetten.overheid.nl",
        "key_statutes": ["Wetboek van Burgerlijke Rechtsvordering (Rv) Art. 700", "Gerechtsdeurwaarderswet"],
        "target_archives": ["Rechtbank Rotterdam Admiralty Docket", "Dutch National Archives"]
    }
}

class LegalDataHunter:
    def __init__(self, output_dir=None):
        self.output_dir = output_dir or os.path.join("W:\\Legal\\US_CUBA", "00_Master_Knowledge_Base", "worldwide_legal_cache")
        os.makedirs(self.output_dir, exist_ok=True)

    def resolve_jurisdiction(self, country_code):
        """Retrieve configured endpoints and statutes for a country code."""
        return JURISDICTION_REGISTRY.get(country_code.upper())

    def normalize_decree_record(self, country_code, decree_title, decree_date, issuing_authority, text_snippet):
        """Standardize a scraped foreign decree or court ruling into an evidentiary vector schema."""
        record = {
            "country_code": country_code.upper(),
            "decree_title": decree_title,
            "decree_date": decree_date,
            "issuing_authority": issuing_authority,
            "text_snippet": text_snippet,
            "harvest_timestamp": datetime.now().isoformat(),
            "sha256_fingerprint": hashlib.sha256(text_snippet.encode('utf-8')).hexdigest()
        }
        return record

    def export_evidence_vector(self, record, filename):
        """Write normalized evidence record to JSON."""
        target_path = os.path.join(self.output_dir, filename)
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        return target_path

if __name__ == "__main__":
    hunter = LegalDataHunter()
    cuba_info = hunter.resolve_jurisdiction("CU")
    print(f"Loaded Jurisdiction: {cuba_info['country']} - Portal: {cuba_info['official_gazette_url']}")
    sample_decree = hunter.normalize_decree_record(
        country_code="CU",
        decree_title="Ley 851 de Nacionalización Forzosa",
        decree_date="1960-07-06",
        issuing_authority="Consejo de Ministros de la República de Cuba",
        text_snippet="Nacionalización mediante expropiación forzosa de los bienes y empresas de personas naturales o jurídicas nacionales de los Estados Unidos de Norteamérica."
    )
    print(f"Normalized Record SHA-256: {sample_decree['sha256_fingerprint']}")
