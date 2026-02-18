# 🔍 Control Gap Analysis: Case 2026-02-17-SEC-01

## 1. Technical Control Gaps (Protocol Bypass)
| Control | Status | Gap Observed |
| :--- | :--- | :--- |
| **SPF/DKIM/DMARC** | **FAIL (Policy Bypass)** | The adversary successfully authenticated their own infrastructure. The gateway prioritized technical validity over sender reputation. |
| **Email Gateway Filtering** | **FAIL** | Use of "Bayesian Poisoning" (hidden prose) successfully lowered the spam score below quarantine thresholds. |
| **URL Reputation** | **FAIL** | Payload hosted on `storage.googleapis.com` leveraged inherent trust of a major CSP to bypass blocklists. |

## 2. Deception Analysis: The "Unsubscribe" Trap
**Observation:** The artifact included a functional "Unsubscribe" link (`hxxps://hsmpllt.com/...`).

**Auditor Analysis:** - **Active Target Validation (ATV):** Attackers use these links as a "heartbeat" signal. Clicking confirms the email address is **active and monitored**, increasing its value for future targeted spear-phishing.
- **Compliance Exploitation:** The attacker exploited the user's expectation of **GDPR/CAN-SPAM** compliance to build a false sense of legitimacy.

## 3. Scraped Identity Injection
**Observation:** The adversary utilized a portion of the recipient's email handle (`[REDACTED]`) in the sender field.

**Auditor Analysis:** This marks a transition from "Mass Phishing" to **Targeted Identity Spoofing**. By mirroring a unique personal identifier, the attacker bypassed the "Stranger-Danger" heuristic. This indicates PII was scraped from public-facing metadata.

## 4. Remediation Recommendations
- **Technical:** Deploy AI-based anomaly detection to flag "Look-alike" sender handles.
- **Administrative:** Update Security Awareness Training (SAT) to specifically address "Unsubscribe" links as reconnaissance vectors.
