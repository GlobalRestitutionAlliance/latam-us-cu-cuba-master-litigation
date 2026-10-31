# OPEN-SOURCE LEGAL TECHNOLOGY & DATA HARVESTING TOOL SUITE
**Location:** `.antigravity/tools/`  
**License:** AGPL-3.0 / Apache-2.0 / MIT (The Open-Source Shield)  
**Status:** FULLY INTEGRATED & PORTABLE  

This suite provides open-source court scrapers, docket harvesters, document automation engines, and legal reasoning benchmark evaluators integrated directly into the Antigravity framework. Built to dismantle document starvation, paywall censorship, and resource asymmetries, this modular architecture is designed for immediate operationalization in the US-Cuba Master Litigation and portable across all subsequent sovereign restitution campaigns (`us-nicaragua-master-litigation`, `us-honduras-master-litigation`, `us-hawaii-master-litigation`, etc.).

---

## Tool Catalog & Architecture

### Category 1: Open Legal Data & Court Scrapers (Bypassing Document Starvation)
1. **Free Law Project & RECAP Harvester (`free-law-recap-harvester`):**
   - **Upstream:** [`freelawproject/courtlistener`](https://github.com/freelawproject/courtlistener) (AGPL-3.0)
   - **Spec:** [`free-law-recap-harvester.yaml`](free-law-recap-harvester.yaml) | **Script:** [`free_law_recap_harvester.py`](free_law_recap_harvester.py)
   - **Function:** Interfaces with CourtListener REST API v4 to bypass PACER paywalls, scrape unsealed federal filings via RECAP, parse standard court citations, and screen judicial financial disclosures for conflicts of interest.

2. **World Wide Law Global Legal Data Hunter (`worldwide-legal-data-hunter`):**
   - **Upstream:** [`worldwidelaw/legal-sources`](https://github.com/worldwidelaw/legal-sources) (MIT)
   - **Spec:** [`worldwide-legal-data-hunter.yaml`](worldwide-legal-data-hunter.yaml) | **Script:** [`worldwide_legal_data_hunter.py`](worldwide_legal_data_hunter.py)
   - **Function:** Automated scraper framework mapping primary legislation, official gazettes (e.g. *Gaceta Oficial de Cuba*, *Boletín Oficial del Estado*, *Registro Público de Panamá*), and foreign appellate dockets across 110+ jurisdictions.

3. **Open Legal Data & Pile-of-Law Corpus Processor (`open-legal-data-corpus`):**
   - **Upstream:** [`openlegaldata/openlegaldata`](https://github.com/openlegaldata/openlegaldata) (MIT / Apache-2.0)
   - **Spec:** [`open-legal-data-corpus.yaml`](open-legal-data-corpus.yaml) | **Script:** [`open_legal_data_corpus.py`](open_legal_data_corpus.py)
   - **Function:** Ingests massive public-interest legal corpora (Pile-of-Law, MultiLegalPile) for offline text mining, extracting named entities, uncompensated confiscation clauses, and sovereign immunity triggers.

### Category 2: Legal Aid & Document Automation Engineering (Scaling Class Actions)
4. **Docassemble Guided Interview & Pleading Assembly Engine (`docassemble-action-engine`):**
   - **Upstream:** [`jhpyle/docassemble`](https://github.com/jhpyle/docassemble) (MIT)
   - **Spec:** [`docassemble-action-engine.yaml`](docassemble-action-engine.yaml) | **Script:** [`docassemble_action_engine.py`](docassemble_action_engine.py)
   - **Function:** Generates court-ready federal class action complaints, exequatur briefs, PCA arbitration notices, and IACHR petitions from guided YAML question flows with multi-language rendering and cryptographic hash attestation.

5. **Justack AI Access-to-Justice Triage Engine (`justack-access-triage`):**
   - **Upstream:** [`justack-ai/website`](https://github.com/justack-ai/website) (AGPL-3.0)
   - **Spec:** [`justack-access-triage.yaml`](justack-access-triage.yaml) | **Script:** [`justack_access_triage.py`](justack_access_triage.py)
   - **Function:** Accessible legal triage platform qualifying unrepresented diaspora heirs and certified claimants, translating complex sovereign immunity doctrines into plain language, and matching claimants to litigation subclasses.

### Category 3: Legal AI, Benchmarks, & LLM-Era Legal Reasoning
6. **Stanford CodeX & RegLab LegalBench IRAC Evaluator (`stanford-legalbench-evaluator`):**
   - **Upstream:** [`HazyResearch/legalbench`](https://github.com/HazyResearch/legalbench) (Apache-2.0)
   - **Spec:** [`stanford-legalbench-evaluator.yaml`](stanford-legalbench-evaluator.yaml) | **Script:** [`stanford_legalbench_evaluator.py`](stanford_legalbench_evaluator.py)
   - **Function:** Rigorous adversarial auditing of legal theories, complaints, and briefs across the IRAC (Issue Spotting, Rule Recall, Rule Application, Conclusion) framework before docket filing.

7. **ICTRecht Legal-GenAI Prompt & Compliance Protocol (`ictrecht-genai-resources`):**
   - **Upstream:** [`ICTRecht/Legal-GenAI-Resources`](https://github.com/ICTRecht/Legal-GenAI-Resources) (CC-BY-SA-4.0 / MIT)
   - **Spec:** [`ictrecht-genai-resources.yaml`](ictrecht-genai-resources.yaml) | **Script:** [`ictrecht_genai_resources.py`](ictrecht_genai_resources.py)
   - **Function:** Zero-tolerance citation validation, anti-hallucination prompt templates, and ethical compliance guardrails ensuring court submissions satisfy Model Rules of Professional Conduct.

---

## How Independent Researchers, Coders & Lawyers Integrate

1. **Leveraging Open APIs for Evidence Gathering:**
   Instead of relying on paywalled or restricted databases, researchers query CourtListener and open legal sources directly to pull unsealed filings, judge disclosure forms, and regulatory gazettes.
2. **Automating Exequatur & International Filings:**
   Using Docassemble and open document assembly pipelines, practitioners can programmatically format multi-lingual international arbitration notices (PCA) and human rights petitions (IACHR) simultaneously.
3. **The Open-Source Shield:**
   All tools, scrapers, and analytical dossiers operate under AGPL-3.0 and open-source licenses, providing decentralized resilience and legal protection against centralized takedown notices.

---

## Multi-Nation Portability

This entire tool suite is architected for immediate transfer into future sovereign restitution repositories targeting Euro-American imperialist subjugation:
- `us-nicaragua-master-litigation` (ICJ Judgment Enforcement, Bryan-Chamorro Treaty)
- `us-honduras-master-litigation` (Banana Republic Concession Expropriations)
- `us-hawaii-master-litigation` (1893 Illegal Overthrow, Crown Lands Breach of Trust)
- `us-panama-master-litigation` (1903 Canal Treaty, 1989 Operation Just Cause)
- `us-philippines-master-litigation` (1898 Treaty of Paris, Colonial Reparations)

See [`cross_nation_toolkit_manifest.yaml`](cross_nation_toolkit_manifest.yaml) for replication instructions.
