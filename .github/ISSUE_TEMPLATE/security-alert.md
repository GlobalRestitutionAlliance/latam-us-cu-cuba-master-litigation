---
name: Security & Integrity Alert
about: Report repository tampering, compromised credentials, or pipeline anomalies
title: "[SECURITY-ALERT]: <Compromised Commit / Vulnerability / Anomaly>"
labels: [security, critical]
assignees: ''
---

### Incident Summary
Describe the observed anomaly, unauthorized commit attempt, or credential compromise:

### Affected Components
- **Commit SHA / Branch:**
- **Modified Files:**
- **Observed Integrity Failure:**

### Proposed Mitigation
- [ ] Hard reset to last verified signed release tag (e.g., `v1.805.0`).
- [ ] Revoke compromised GPG key in `VERIFICATION_KEYS/maintainers.asc`.
- [ ] Trigger Reversion Protocol across all decentralized mirrors.
