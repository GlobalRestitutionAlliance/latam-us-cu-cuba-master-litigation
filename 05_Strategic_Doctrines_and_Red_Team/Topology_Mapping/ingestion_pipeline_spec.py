"""
IRS Form 990 / Grant Registry Graph Ingestion Pipeline Specification
Parses public XML / JSON datasets and loads graph topology into Neo4j.
"""

import hashlib
from typing import Dict, List, Any

def generate_grant_id(donor_ein: str, recipient_ein: str, tax_year: int, amount: float) -> str:
    raw = f"{donor_ein}_{recipient_ein}_{tax_year}_{amount:.2f}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

def generate_person_id(name: str) -> str:
    clean = "".join(c.lower() for c in name if c.isalnum())
    return hashlib.sha256(clean.encode("utf-8")).hexdigest()[:16]

def calculate_herfindahl_index(grant_amounts: List[float], total_external_revenue: float) -> float:
    """
    Computes normalized Herfindahl-Hirschman Index (HHI) for funding concentration.
    Values range from 0.0 (perfectly diversified) to 1.0 (single-source dependency).
    """
    if not grant_amounts or total_external_revenue <= 0:
        return 0.0
    shares = [amt / total_external_revenue for amt in grant_amounts]
    raw_hhi = sum(s ** 2 for s in shares)
    n = len(grant_amounts)
    if n <= 1:
        return 1.0
    normalized_hhi = (raw_hhi - (1.0 / n)) / (1.0 - (1.0 / n))
    return max(0.0, min(1.0, normalized_hhi))

if __name__ == "__main__":
    print("Graph Ingestion Pipeline Module Loaded successfully.")
