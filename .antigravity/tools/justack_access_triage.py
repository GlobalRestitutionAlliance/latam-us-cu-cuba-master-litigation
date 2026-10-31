#!/usr/bin/env python3
"""
Justack AI Access-to-Justice Triage Engine
Claimant Qualification, Rights Assessment & Subclass Matching
"""

import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

class JustackTriage:
    def __init__(self):
        self.subclasses = {
            "subclass_1": "Historic Expropriated Industrial & Utility Holdings (Pre-1959 Title V)",
            "subclass_2": "Transnational Sovereign Commercial Monopolies & State Alter Ego Disgorgement",
            "subclass_3": "Maritime, Port Towage, Subsea Fiber & Logistics Concessions",
            "subclass_4": "Continuous Fiduciary & Territorial Breaches (1805–2026 Continuum)"
        }

    def evaluate_claimant(self, profile):
        """
        Evaluate claimant profile and assign subclass & eligibility status.
        profile: dict with keys:
          - has_fcsc_award: bool
          - property_type: str ('utility', 'real_estate', 'maritime', 'telecom', 'territorial')
          - trafficking_observed: bool
          - nationality: str ('US', 'Dual', 'Foreign')
        """
        eligibility = {
            "eligible": False,
            "assigned_subclass": None,
            "statutory_pathways": [],
            "restitution_readiness_score": 0.0
        }

        score = 0.0
        if profile.get("has_fcsc_award"):
            score += 0.4
            eligibility["statutory_pathways"].append("Title V Certified Claim Precedent (FCSC)")
        
        if profile.get("trafficking_observed"):
            score += 0.3
            eligibility["statutory_pathways"].append("Helms-Burton Act Title III (22 U.S.C. § 6082)")

        prop_type = profile.get("property_type", "").lower()
        if prop_type in ["utility", "industrial", "sugar", "mining", "rum"]:
            eligibility["assigned_subclass"] = self.subclasses["subclass_1"]
            score += 0.3
        elif prop_type in ["telecom", "banking", "retail", "pharma"]:
            eligibility["assigned_subclass"] = self.subclasses["subclass_2"]
            score += 0.3
        elif prop_type in ["maritime", "port", "subsea_cable", "shipping"]:
            eligibility["assigned_subclass"] = self.subclasses["subclass_3"]
            score += 0.3
        elif prop_type in ["territorial", "fiduciary"]:
            eligibility["assigned_subclass"] = self.subclasses["subclass_4"]
            score += 0.3

        eligibility["restitution_readiness_score"] = min(1.0, score)
        eligibility["eligible"] = score >= 0.5

        return eligibility

if __name__ == "__main__":
    triage = JustackTriage()
    test_claimant = {
        "has_fcsc_award": True,
        "property_type": "telecom",
        "trafficking_observed": True,
        "nationality": "US"
    }
    result = triage.evaluate_claimant(test_claimant)
    print("Triage Result:")
    print(f" - Eligible: {result['eligible']}")
    print(f" - Subclass: {result['assigned_subclass']}")
    print(f" - Score: {result['restitution_readiness_score'] * 100:.1f}%")
    print(f" - Pathways: {', '.join(result['statutory_pathways'])}")
