# NETWORK TOPOLOGY & PROVENANCE MAPPING SCHEMA

**TECHNICAL SPECIFICATION & DATA ARCHITECTURE**  
**ENGINE:** Graph Database (Neo4j / Labeled Property Graph)  
**PRIMARY DATA INGESTION:** Public Regulatory Disclosures (IRS Form 990 / 990-PF Series, USASpending.gov, SEC Form 4/14A)  

---

## 1. ARCHITECTURAL OVERVIEW & OBJECTIVE

The Network Topology & Provenance Mapping Schema defines a graph database architecture engineered to map financial flows, institutional dependencies, and governance overlaps among corporate, philanthropic, and non-profit entities using publicly available records.

Primary data sources include public regulatory filings: IRS Form 990, 990-PF, and 990-EZ e-file XML datasets (released via AWS Registry of Open Data and the IRS e-file portal), USASpending.gov federal award databases, SEC proxy statements (Schedule 14A), and state charity registries.

By modeling institutional entities and individuals within a labeled property graph (LPG), analytical queries can trace capital trajectories, calculate network concentration metrics, and evaluate structural independence.

## 2. LABELED PROPERTY GRAPH (LPG) SCHEMA DEFINITIONS

**A. NODE DEFINITIONS:**

1. :Organization
   - Properties: ein (String, Unique), legal_name (String), dba_name (String), entity_type (String, e.g., '501(c)(3)', '501(c)(4)', 'Corporation'), formation_year (Integer), state_jurisdiction (String), total_revenue (Float), total_assets (Float), ntee_code (String).

2. :Person
   - Properties: person_id (String, Unique Hash), full_name (String), normalized_name (String), bio_identifier (String).

3. :Grant
   - Properties: grant_id (String, Unique Hash), tax_year (Integer), amount (Float), grant_purpose (String), source_document (String).

4. :Filing
   - Properties: filing_id (String, Unique), ein (String), tax_year (Integer), form_type (String), total_contributions (Float), gross_receipts (Float), file_url (String).

**B. RELATIONSHIP DEFINITIONS:**

1. (:Organization)-[:AWARDED_GRANT]->(:Grant)
   - Denotes an institutional donor originating a charitable contribution or institutional grant.

2. (:Grant)-[:DISBURSED_TO]->(:Organization)
   - Denotes the recipient organization receiving the grant allocation.

3. (:Person)-[:SERVES_ON {role: String, title: String, compensation: Float, hours_per_week: Float, tax_year: Integer}]->(:Organization)
   - Models officer, director, trustee, and key employee relationships reported in Form 990 Part VII.

4. (:Organization)-[:FILED_DOCUMENT]->(:Filing)
   - Associates annual regulatory filings with the respective legal entity.

5. (:Organization)-[:AFFILIATED_WITH {relationship_type: String, ownership_pct: Float}]->(:Organization)
   - Models parent-subsidiary, joint-venture, and brother-sister corporate affiliations reported in Schedule R.

## 3. MATHEMATICAL FORMULATION: CENTRALIZATION & DEPENDENCY COEFFICIENTS

To quantify an entity's structural dependency on specific funding sources or centralized institutional networks, the schema implements three algorithmic metrics:

**A. FUNDING CONCENTRATION (HERFINDAHL-HIRSCHMAN INDEX - HHI):**

Let an organization O receive external funding from n distinct institutional donors. Let s_i denote the fractional share of grant i relative to total institutional revenue R_total:
   s_i = Amount(Grant_i) / R_total
The normalized funding Herfindahl-Hirschman Index (H_fund) is calculated as:
   H_fund = (SUM(s_i^2) - 1/n) / (1 - 1/n) for n > 1, and 1.0 for n = 1.
An H_fund approaching 1.0 indicates near-total dependency on a single funding node, whereas values below 0.15 indicate a widely diversified funding base.

**B. WEIGHTED IN-DEGREE CENTRALITY & FUNDER EIGENVECTOR INFLUENCE:**

To evaluate whether an entity's funding originates from high-degree macro-funders, the schema computes an Eigenvector-Weighted Funding Metric (E_fund):
   E_fund(O) = SUM(s_i * EigenvectorCentrality(Donor_i))
where EigenvectorCentrality(Donor_i) represents the donor's relative influence within the global bipartite grant network.

**C. GOVERNANCE INTERLOCK INDEX (BOARD OVERLAP):**

Let B(O) be the set of individuals serving on the board of organization O. The Governance Interlock Index (G_interlock) with respect to a target cohort of institutions C is defined as:
   G_interlock(O, C) = |B(O) INTERSECT B(C)| / |B(O)|
This ratio quantifies the proportion of governing fiduciaries who hold simultaneous fiduciary appointments across other designated institutions.

**D. COMPOSITE CENTRALIZATION COEFFICIENT (C_coeff):**

Combining financial concentration, funder centrality, and governance interlocks yields a normalized index [0.0, 1.0]:
   C_coeff(O) = w_1 * H_fund + w_2 * E_fund + w_3 * G_interlock
where w_1 = 0.40, w_2 = 0.35, and w_3 = 0.25 (calibrated to reflect relative structural impact).

## 4. CYPHER QUERY SPECIFICATIONS & ANALYTICAL PIPELINE

**A. IDENTIFYING DOMINANT SINGLE-SOURCE FUNDERS:**

MATCH (donor:Organization)-[:AWARDED_GRANT]->(g:Grant)-[:DISBURSED_TO]->(target:Organization)
WHERE target.ein = $target_ein
WITH donor, sum(g.amount) AS total_from_donor, target.total_revenue AS rev
RETURN donor.legal_name, total_from_donor, (total_from_donor / rev) AS funding_ratio
ORDER BY funding_ratio DESC LIMIT 10;

**B. DETECTING INTERLOCKING DIRECTORATES (SHARED BOARD MEMBERS):**

MATCH (p:Person)-[:SERVES_ON]->(orgA:Organization)
MATCH (p)-[:SERVES_ON]->(orgB:Organization)
WHERE orgA <> orgB
RETURN p.normalized_name, orgA.legal_name, orgB.legal_name, count(*) AS shared_roles
ORDER BY shared_roles DESC;

**C. TRANSITIVE CAPITAL PATH TRACING (MULTI-TIER PASS-THROUGH):**

MATCH path = (origin:Organization)-[:AWARDED_GRANT*2..4]->(destination:Organization)
WHERE origin.ein = $source_ein AND destination.ein = $dest_ein
RETURN path, length(path) AS tiers
LIMIT 25;

## 5. DATA INTEGRITY, ETHICAL GOVERNANCE & VERIFICATION

All analysis conducted under this schema must rely exclusively on publicly disclosed regulatory filings (e.g., IRS Form 990 Schedule I grant tables, Schedule B non-confidential schedules, and public disclosure APIs).

Network analysis metrics are diagnostic structural indicators of institutional funding concentration and governance connectivity. They measure financial provenance and administrative interlock; they do not imply unlawful conduct or coordination beyond verifiable statutory reporting.

Data records must maintain full cryptographic hashes of primary source XML and PDF filings to guarantee chain-of-custody and prevent data modification.

