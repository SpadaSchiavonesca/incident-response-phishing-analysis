# 🛡️ Security Incident Investigation & Control Validation

> **Focus:** Targeted Phishing, Infrastructure Forensics & GRC Framework Mapping (NIST/ISO)

---

## 📋 Executive Overview

This repository documents a high-sophistication, targeted phishing campaign (Incident `2026-02-17-SEC-01`) analyzed through the lens of **IT Audit and GRC**. The investigation demonstrates the adversarial transition from opportunistic mass-phishing to **Targeted Identity Spoofing**, leveraging authenticated attacker infrastructure to bypass traditional security perimeters.

### 🔑 Key Findings

| # | Finding | Detail |
|---|---|---|
| 1 | **Protocol Failure** | SPF/DKIM/DMARC returned `PASS` — confirming advanced technical maturity of the adversary. |
| 2 | **Tactic Identification** | Confirmed use of **Bayesian Poisoning** and **Active Target Validation (ATV)** via deceptive "Unsubscribe" links. |
| 3 | **Identity Injection** | Attacker programmatically mirrored recipient handle `[REDACTED]` to bypass cognitive security heuristics. |

---

## 📂 Investigation Lifecycle

<details>
<summary>🔵 Phase 1 — Identification & Evidence Collection</summary>

**Artifact Link:** [`evidence/sanitized_headers.txt`](evidence/sanitized_headers.txt)

- **Artifacts:** Sanitized SMTP headers and delivery metadata.
- **Forensics:** Traced anomalous multi-hop routing path — `US → UA → BR`.

</details>

<details>
<summary>🟡 Phase 2 — Qualitative Risk Assessment</summary>

**Artifact Link:** [`investigations/risk-assessment.md`](investigations/risk-assessment.md)

- **Framework:** NIST SP 800-30.
- **Analysis:** Evaluation of **Likelihood vs. Impact** matrix to determine final risk rating of `Medium / High`.

</details>

<details>
<summary>🟠 Phase 3 — Formal Gap Analysis</summary>

**Artifact Link:** [`investigations/gap-analysis.md`](investigations/gap-analysis.md)

- **Framework:** NIST CSF / SP 800-53.
- **Deep Dive:** Technical audit of control failures (AC-04, SC-07, SI-08) and the "Unsubscribe" reconnaissance loop.

</details>

<details>
<summary>✅ Phase 4 — Remediation & Mitigation</summary>

**Artifact Link:** [`investigations/mitigation-report.md`](investigations/mitigation-report.md)

- **Status:** `CLOSED`
- **Corrective Actions:** Transition to Authenticated Identity Proxies and FIDO2/WebAuthn credential hardening.

</details>

---

## 🛠️ Frameworks & Standards

| Framework | Application |
|---|---|
| **NIST SP 800-61 Rev. 2** | Incident Handling Lifecycle |
| **MITRE ATT&CK®** | Adversary tactic and technique mapping |
| **NIST SP 800-30** | Risk assessment methodology |
| **NIST SP 800-53** | Control identification and gap analysis |
| **CAN-SPAM / GDPR** | Regulatory compliance analysis of deceptive link mechanics |

---

## 👤 Auditor

**Nenad Uzelac** — *GRC & IT Audit Professional*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nenad%20Uzelac-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/uzelac-nenad/)
[![GitHub](https://img.shields.io/badge/GitHub-SpadaSchiavonesca-181717?style=flat&logo=github&logoColor=white)](https://github.com/SpadaSchiavonesca)

---

<details>
<summary>📋 Document Metadata</summary>

| Field | Value |
|---|---|
| Incident Reference | `2026-02-17-SEC-01` |
| Report Status | `Finalized` |
| Classification | `Internal` |
| Frameworks Referenced | NIST SP 800-61, 800-30, 800-53, MITRE ATT&CK, CAN-SPAM, GDPR |
| Last Updated | 2026-02-18 |

</details>
