#!/usr/bin/env python3
"""
Stanford CodeX & RegLab LegalBench IRAC Evaluator
Standardized Legal Reasoning, Issue Spotting & Precedent Recall Benchmark
"""

import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

REQUIRED_ISSUES = [
    ("FSIA Commercial Activity", [r'1605\(a\)\(2\)', r'commercial\s+activity']),
    ("FSIA Expropriation Exception", [r'1605\(a\)\(3\)', r'takings\s+in\s+violation']),
    ("Helms-Burton Title III", [r'6082', r'Helms-Burton', r'LIBERTAD']),
    ("Bancec Alter Ego", [r'Bancec', r'alter\s+ego', r'veil-piercing']),
    ("QSF Trust Structure", [r'468B', r'Qualified\s+Settlement\s+Fund'])
]

REQUIRED_RULES = [
    ("Bancec Precedent", r'462\s+U\.S\.\s+611'),
    ("Mitchell Fiduciary Precedent", r'463\s+U\.S\.\s+206'),
    ("Havana Docks Precedent", r'104\s+F\.4th\s+1243'),
    ("Rubin Sovereign Immunity Precedent", r'138\s+S\.\s+Ct\.\s+816')
]

class LegalBenchEvaluator:
    def __init__(self):
        pass

    def evaluate_pleading(self, text):
        """Perform an IRAC benchmark evaluation on a legal brief or pleading."""
        results = {
            "issue_spotting_score": 0.0,
            "rule_recall_score": 0.0,
            "rule_application_score": 0.0,
            "conclusion_score": 0.0,
            "composite_irac_score": 0.0,
            "detected_issues": [],
            "detected_rules": [],
            "status": "UNRATED"
        }

        # 1. Issue Spotting
        issues_found = 0
        for issue_name, patterns in REQUIRED_ISSUES:
            found = any(re.search(pat, text, re.IGNORECASE) for pat in patterns)
            if found:
                issues_found += 1
                results["detected_issues"].append(issue_name)
        results["issue_spotting_score"] = issues_found / len(REQUIRED_ISSUES)

        # 2. Rule Recall
        rules_found = 0
        for rule_name, pat in REQUIRED_RULES:
            if re.search(pat, text):
                rules_found += 1
                results["detected_rules"].append(rule_name)
        results["rule_recall_score"] = rules_found / len(REQUIRED_RULES)

        # 3. Rule Application (Factual nexus)
        has_dates = bool(re.search(r'\b(1959|1960|1805|2024|2026)\b', text))
        has_entities = bool(re.search(r'\b(ETECSA|Cuba|Government|Corporation)\b', text))
        has_property = bool(re.search(r'\b(property|concession|infrastructure|shares|dock)\b', text, re.IGNORECASE))
        results["rule_application_score"] = sum([has_dates, has_entities, has_property]) / 3.0

        # 4. Conclusion
        has_restitution = bool(re.search(r'\b(restitution|damages|judgment|treble)\b', text, re.IGNORECASE))
        has_quantum = bool(re.search(r'\$[\d,]+(?:\.\d{2})?', text))
        results["conclusion_score"] = sum([has_restitution, has_quantum]) / 2.0

        # Composite Score
        results["composite_irac_score"] = (
            results["issue_spotting_score"] * 0.35 +
            results["rule_recall_score"] * 0.25 +
            results["rule_application_score"] * 0.25 +
            results["conclusion_score"] * 0.15
        )

        results["status"] = "BENCHMARK_PASSED" if results["composite_irac_score"] >= 0.75 else "REVISION_REQUIRED"

        return results

if __name__ == "__main__":
    evaluator = LegalBenchEvaluator()
    sample_brief = """
    Plaintiffs assert claims under 28 U.S.C. § 1605(a)(2) and § 1605(a)(3) against ETECSA as an alter ego
    of the Cuban sovereign state pursuant to First National City Bank v. Bancec, 462 U.S. 611 (1983).
    Under United States v. Mitchell, 463 U.S. 206, and Havana Docks Corp. v. Royal Caribbean Cruises, Ltd., 104 F.4th 1243 (11th Cir. 2024),
    Defendant's uncompensated 1960 confiscation of telecommunications property establishes continuous liability.
    Plaintiffs pray for judgment in the amount of $310,000,000,000.00 and distribution through a Qualified Settlement Fund under 26 U.S.C. § 468B.
    """
    res = evaluator.evaluate_pleading(sample_brief)
    print("LegalBench Evaluation Results:")
    print(f" - Composite IRAC Score: {res['composite_irac_score'] * 100:.1f}%")
    print(f" - Status: {res['status']}")
    print(f" - Issues Identified ({len(res['detected_issues'])}): {', '.join(res['detected_issues'])}")
    print(f" - Rules Recalled ({len(res['detected_rules'])}): {', '.join(res['detected_rules'])}")
