#!/usr/bin/env python3
"""
Open Legal Data & Pile-of-Law Corpus Processor
Forensic Mining, Named Entity Extraction & Legal Corpus Tokenization
"""

import sys
import os
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

SOVEREIGN_PATTERNS = [
    r'(?:Republic|State|Government)\s+of\s+([A-Z][a-zA-Z\s]+)',
    r'(?:Ministry|Ministerio)\s+(?:of|de)\s+([A-Z][a-zA-Z\s]+)',
    r'([A-Z][a-zA-Z\s]+)\s+(?:S\.A\.|Corp\.|Inc\.|LLC|Holding)',
    r'FCSC\s+Claim\s+No\.\s+([A-Z0-9\-]+)'
]

STATUTORY_VIOLATION_PATTERNS = [
    r'(?:confiscated|expropriated|nationalized)\s+(?:without\s+compensation|under\s+Law\s+\d+)',
    r'(?:trafficking|trafficked)\s+in\s+confiscated\s+property',
    r'28\s+U\.S\.C\.\s+§?\s*1605\([a-z]\)\(\d+\)',
    r'22\s+U\.S\.C\.\s+§?\s*6082'
]

class CorpusProcessor:
    def __init__(self, corpus_root=None):
        self.corpus_root = corpus_root or os.path.join("W:\\Legal\\US_CUBA", "00_Master_Knowledge_Base")

    def extract_entities(self, text):
        """Extract sovereign entities, corporate alter egos, and FCSC claim references."""
        entities = set()
        for pat in SOVEREIGN_PATTERNS:
            for match in re.finditer(pat, text):
                entities.add(match.group(0).strip())
        return sorted(list(entities))

    def detect_statutory_triggers(self, text):
        """Scan text for statutory hooks (FSIA, Helms-Burton, Law 851 confiscations)."""
        triggers = []
        for pat in STATUTORY_VIOLATION_PATTERNS:
            matches = re.findall(pat, text, re.IGNORECASE)
            if matches:
                triggers.extend(matches)
        return sorted(list(set(triggers)))

    def chunk_document(self, text, max_words=500):
        """Segment a long legal document into semantic paragraph blocks for vector indexing."""
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = []
        current_word_count = 0

        for p in paragraphs:
            words = p.split()
            if not words:
                continue
            if current_word_count + len(words) > max_words and current_chunk:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = [p]
                current_word_count = len(words)
            else:
                current_chunk.append(p)
                current_word_count += len(words)

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        return chunks

if __name__ == "__main__":
    processor = CorpusProcessor()
    sample_text = """
    The Government of Cuba and the Ministry of Communications nationalized the assets of International Telephone & Telegraph Corp. under Law 851 without compensation.
    Claimant holds certified award FCSC Claim No. CU-2615. Defendant ETECSA is trafficking in confiscated property in direct violation of 22 U.S.C. § 6082
    and subject to federal jurisdiction under 28 U.S.C. § 1605(a)(3).
    """
    entities = processor.extract_entities(sample_text)
    triggers = processor.detect_statutory_triggers(sample_text)
    print("Extracted Entities:", entities)
    print("Detected Statutory Triggers:", triggers)
