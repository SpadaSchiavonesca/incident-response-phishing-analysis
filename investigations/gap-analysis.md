# 🔍 Gap Analysis: Control Effectiveness & Vulnerability Assessment

> **Incident Ref:** `2026-02-17-SEC-01` &nbsp;|&nbsp; **Status:** `Finalized` &nbsp;|&nbsp; **Classification:** `Internal`

---

## 1. Control Effectiveness Summary

This section evaluates the performance of the technical security stack against the specific adversarial tactics identified during the investigation.

| Control Identifier | Control Name | Status | Audit Finding |
|---|---|---|---|
| `NIST AC-04` | Email Authentication | 🔴 **INADEQUATE** | RFC-compliant SPF/DKIM/DMARC signatures were present on the malicious domain, successfully neutralizing reputation-based gateway filters. |
| `NIST SC-07` | Boundary Protection | 🟠 **BYPASSED** | Adversary utilized "Living off the Land" (LotL) tactics via `storage.googleapis.com` to leverage high-reputation CSP infrastructure and bypass domain blacklists. |
| `NIST SI-08` | Spam/Phishing Detection | 🟠 **BYPASSED** | "Bayesian Poisoning" (large blocks of legitimate prose) was used to dilute the spam-probability scoring of the content engine. |



---

## 2. Behavioral Analysis: The "Unsubscribe" Reconnaissance Loop

A high-priority finding was the inclusion of a functional "Unsubscribe" mechanism (`hxxps://hsmpllt[.]com/...`).

> **⚠️ Auditor's Note — Active Target Validation (ATV)**
>
> In a targeted campaign, the "Unsubscribe" link is **not** a compliance feature; it is an **active heartbeat monitor**. Clicking this link confirms the recipient handle is valid, monitored, and reactive.

* **Data Enrichment:** Interaction signals to the adversary that the PII associated with this handle has a high "Return on Investment" (ROI), likely triggering secondary, high-sophistication spear-phishing attempts.
* **Regulatory Masquerade:** The adversary intentionally exploited the user's expectation of CAN-SPAM/GDPR compliance to mask a reconnaissance operation as a legitimate administrative function.

---

## 3. Vulnerability Root Cause: Identity Mirroring

The adversary demonstrated a transition from opportunistic phishing to **Targeted Identity Spoofing**.

* **The Injection:** The attacker programmatically scraped the unique identifier `[REDACTED]` and injected it into the `Envelope-From`, `Display Name`, and `List-ID` fields.
* **Root Cause:** PII exposure in public-facing metadata provided the "seed data" for this automation.
* **Impact:** This bypasses the Cognitive Heuristic of *"Stranger Danger,"* as the user sees a familiar personal identifier associated with the threat.
  

### 📸 Forensic Evidence (Sanitized)
To validate the technical maturity of the adversary, I performed a manual review of the primary artifacts.

**Figure 1: Email Inbox View (Social Engineering & Urgency)**
![Sanitized Inbox View](https://raw.githubusercontent.com/SpadaSchiavonesca/incident-response-phishing-analysis/main/evidence/evidence-inbox-sanitized.png)
*Observation: The subject line utilizes high-pressure tactics (7-hour deadline) to force user execution.*

**Figure 2: Authentication Results (Technical Control Bypass)**
![Sanitized Header View](https://raw.githubusercontent.com/SpadaSchiavonesca/incident-response-phishing-analysis/main/evidence/evidence-headers-auth-pass.png)
*Observation: Critical email authentication controls (SPF, DKIM, and DMARC) all returned a PASS status.*

---

## 4. Corrective Action Plan (CAP)

Based on the identified gaps, the following remediation is mandated to align with **NIST CSF (Detect/Protect)**:

| Priority | Domain | Action |
|---|---|---|
| 🔴 High | **Administrative** | Transition all public-facing contact metadata to an Authenticated Identity Gateway (LinkedIn Vanity URL). |
| 🔴 High | **Technical** | Enforce FIDO2/WebAuthn hardware tokens to negate the utility of successfully harvested credentials. |
| 🟡 Medium | **UAT (Awareness)** | Update User Awareness Training specifically on the "Unsubscribe Reconnaissance" vector and identity-mirroring detection. |

---

<details>
<summary>📋 Document Metadata</summary>

| Field | Value |
|---|---|
| Incident Reference | `2026-02-17-SEC-01` |
| Report Status | Finalized |
| Classification | Internal |
| Frameworks Referenced | NIST SP 800-53, NIST CSF, CAN-SPAM, GDPR |
| Last Updated | 2026-02-18 |

</details>
