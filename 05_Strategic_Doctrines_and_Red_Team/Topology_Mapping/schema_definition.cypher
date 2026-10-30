// UNIQUE CONSTRAINTS
CREATE CONSTRAINT unique_org_ein IF NOT EXISTS FOR (o:Organization) REQUIRE o.ein IS UNIQUE;
CREATE CONSTRAINT unique_person_id IF NOT EXISTS FOR (p:Person) REQUIRE p.person_id IS UNIQUE;
CREATE CONSTRAINT unique_grant_id IF NOT EXISTS FOR (g:Grant) REQUIRE g.grant_id IS UNIQUE;
CREATE CONSTRAINT unique_filing_id IF NOT EXISTS FOR (f:Filing) REQUIRE f.filing_id IS UNIQUE;

// SEARCH & LOOKUP INDEXES
CREATE INDEX org_name_idx IF NOT EXISTS FOR (o:Organization) ON (o.legal_name);
CREATE INDEX person_name_idx IF NOT EXISTS FOR (p:Person) ON (p.normalized_name);
CREATE INDEX grant_year_idx IF NOT EXISTS FOR (g:Grant) ON (g.tax_year);
CREATE INDEX filing_tax_year_idx IF NOT EXISTS FOR (f:Filing) ON (f.tax_year);

// ANALYTICAL QUERY: COMPOSITE DEPENDENCY METRIC
MATCH (donor:Organization)-[:AWARDED_GRANT]->(g:Grant)-[:DISBURSED_TO]->(target:Organization)
WHERE target.ein = $target_ein AND target.total_revenue > 0
WITH donor, sum(g.amount) AS donor_total, target.total_revenue AS rev
RETURN donor.legal_name AS donor_name,
       donor_total,
       (donor_total / rev) AS funding_dependency_ratio
ORDER BY funding_dependency_ratio DESC;
