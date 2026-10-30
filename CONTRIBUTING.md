# CONTRIBUTION PROTOCOL

## Who May Participate
- Civil rights and impact litigation counsel
- Archival researchers and historians
- Cryptographers, data engineers, and security specialists
- Subclass representatives and affected communities
- International law scholars and tribunal advocates

## Contribution Rules
1. **Mandatory GPG Signing:** All commits MUST be cryptographically signed with a valid GPG key.
2. **Primary Source Evidentiary Standard:** All factual and evidentiary submissions MUST include primary source citations (NARA, Library of Congress, foreign national archives, or certified judicial dockets).
3. **Continuous Hash Integrity:** All pull requests MUST pass automated CI verification against `VERIFICATION_KEYS/sha256_manifest.txt`.
4. **CODEOWNERS Review:** Changes to domain directories require formal sign-off from designated maintainers.
5. **No Anonymous Direct Pushes:** All changes must proceed through pull requests with linear history.

## Submitting an Evidentiary Vector
1. Fork the repository on GitHub (`https://github.com/GlobalRestitutionAlliance/us-cuba-master-litigation`).
2. Create a feature branch: `git checkout -b vector/submission-XXXX`.
3. Add your vector to the appropriate YAML file in `.antigravity/knowledge/vector-index/`.
4. Update `VERIFICATION_KEYS/sha256_manifest.txt` with the new file hashes.
5. Sign your commit: `git commit -S -m "feat: submit vector XXXX - [Description]"`.
6. Open a pull request using the `vector-submission` template.

## Security Reporting
If you detect an integrity breach, compromised maintainer key, or attempted repository tampering, immediately follow [`SECURITY.md`](SECURITY.md).
