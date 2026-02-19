#!/bin/bash
# Phishing Incident Triage Script
# Target IoC: humplt[.]com (Malicious 'Unsubscribe' Heartbeat Domain)

echo "--- 🔍 Starting System Log Triage ---"

# This command searches common Linux log directories for the IoC
# It mimics the manual search you would perform during an audit
grep -r "humplt.com" /var/log/ 2>/dev/null

if [ $? -eq 0 ]; then
    echo "[!] ALERT: Indicator of Compromise (IoC) found in system logs."
    echo "[*] GRC Note: Potential unauthorized network connection detected."
else
    echo "[+] Clean: No interaction with known heartbeat domain detected."
fi
