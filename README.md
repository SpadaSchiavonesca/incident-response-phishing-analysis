# 🛡️ Governance, Risk, & Compliance (GRC) | Incident Case Study
**Project:** Targeted Identity-Mirroring & Infrastructure Forensics  
**Frameworks:** NIST SP 800-61, NIST CSF, MITRE ATT&CK®, ISO/IEC 27001  
**Investigator:** [Nenad Uzelac]((https://www.linkedin.com/in/nenaduzelac/))

---

## 📋 Executive Summary
This repository documents a high-sophistication, targeted phishing campaign (Incident `2026-02-17-SEC-01`) analyzed through the lens of **IT Audit and GRC**. The investigation demonstrates the transition from opportunistic "mass-phishing" to **Targeted Identity Spoofing**, leveraging authenticated attacker infrastructure to bypass traditional security perimeters.

### 🔑 Critical Audit Findings
* **Protocol Failure:** SPF/DKIM/DMARC returned **PASS** results, proving technical maturity of the adversary and the inadequacy of reputation-only filters.
* **Tactic Identification:** Confirmed use of **Bayesian Poisoning** and **Active Target Validation (ATV)** via deceptive "Unsubscribe" links.
* **Identity Injection:** The attacker programmatically mirrored the recipient's unique handle `[REDACTED]` to bypass cognitive security heuristics.

---

## 📂 Investigative Lifecycle & Documentation
Access the formal audit trail through the following phases:

### 📑 [Phase 1: Forensic Artifact Collection](./evidence/raw_headers.txt)
* **Metadata Analysis:** Sanitized SMTP headers documenting the anomalous routing path (US -> UA -> BR).
* **Infrastructure Trace:** Tracing the origin to a DigitalOcean node via a compromised Brazilian educational relay.

### 📑 [Phase 2: Qualitative Risk Assessment](investigations/risk-assessment.md)
* **Methodology:** Conducted via **NIST SP 800-30** standards.
* **Risk Determination:** Evaluation of **Likelihood vs. Impact** resulting in a Medium/High risk rating.

### 📑 [Phase 3: Control Gap Analysis](investigations/gap-analysis.md)
* **Deep Dive:** Technical audit of control failures regarding **NIST AC-04** and **SC-07**.
* **Special Finding:** Analysis of the "Unsubscribe" loop as a reconnaissance and target validation vector.

### 📑 [Phase 4: Remediation & PIR](investigations/mitigation-report.md)
* **Status:** 🟢 **CLOSED** - Mitigations Implemented.
* **CAP (Corrective Action Plan):** Transition to Authenticated Identity Proxies and FIDO2 hardware hardening.

---

## 🛠️ Standards & Compliance Mapping
| Domain | Standard / Framework |
| :--- | :--- |
| **Incident Handling** | NIST SP 800-61 Rev. 2 |
| **Adversary Tactics** | MITRE ATT&CK® |
| **Risk Management** | NIST SP 800-30 |
| **Regulatory Privacy** | CAN-SPAM / GDPR (Compliance Exploitation) |

---

## 👤 Professional Connectivity
**Nenad Uzelac** *GRC and IT Audit*
[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nenaduzelac/)
[![GitHub Profile](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SpadaSchiavonesca)
