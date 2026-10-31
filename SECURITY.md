# SECURITY POLICY & REVERSION PROTOCOL

## Threat Model & Defensive Posture
The repository operates under a Zero-Trust Model designed to protect evidentiary integrity against unauthorized alteration, silent corruption, or centralized takedown.

## Reporting a Security Vulnerability or Breach
If you discover a security vulnerability, compromised signing key, or unauthorized commit:
1. **Do not create a public issue.**
2. Submit a confidential report via GitHub Private Vulnerability Reporting / Security Advisories.
3. For immediate CI alert notifications, utilize the `[SECURITY-ALERT]` issue template.

## The Reversion Protocol (Anti-Derailment Maneuver)
If a malicious or corrupted commit bypasses checks and merges into `main`:
1. **Identify the Last Verified Milestone:**
   ```bash
   git tag --list "v*" --sort=-v:refname | head -n 1
   ```
2. **Verify Tag Cryptographic Signature:**
   ```bash
   git tag -v v1.0.1
   ```
3. **Execute Local Hard Reset:**
   ```bash
   git checkout main
   git reset --hard v1.0.1
   ```
4. **Synchronize Force-Reset Across All Mirrors:**
   ```bash
   git push origin main --tags --force
   git push gitlab main --tags --force
   git push codeberg main --tags --force
   ```
5. **Publish Public Audit Incident Notice** documenting the reverted commit hash and restored state.
