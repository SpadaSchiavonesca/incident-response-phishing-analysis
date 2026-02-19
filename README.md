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

## 🛠️ Investigation Toolbox & Skills

| **Category** | **Tools & Techniques** |
|--------------|------------------------|
| **🔍 Forensics** | SMTP Header Analysis, WHOIS Research, IP Geolocation |
| **⚖️ Risk Management** | NIST SP 800-30 Qualitative Assessment, Risk Matrix Modeling |
| **📋 Compliance** | NIST CSF Mapping, GDPR & CAN-SPAM Regulatory Review |
| **🛡️ Security Ops** | Phishing Triage, Email Gateway Bypass Analysis (SPF/DKIM/DMARC) |

---

## 👤 Professional Connectivity

**Nenad Uzelac**  
*GRC Analyst | IT Audit Professional | Cybersecurity Researcher*

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nenad_Uzelac-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nenaduzelac/)
[![GitHub](https://img.shields.io/badge/GitHub-SpadaSchiavonesca-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SpadaSchiavonesca)

</div>

---

## 📄 License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

> This project is licensed under the **MIT License** - click the badge above to view the full audit terms in the `LICENSE` file.


