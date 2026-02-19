import re
import os

def run_forensic_simulation(file_path):
    try:
        # We use a relative path so the script works inside the GitHub folder structure
        with open(file_path, 'r') as file:
            data = file.read()
            
        print(f"--- 🔍 Analyzing Artifact: {file_path} ---")
        
        # Logic 1: Detect the 'Triple Pass' Reputation Bypass (NIST AC-04)
        auth_results = re.findall(r'(spf=pass|dkim=pass|dmarc=pass)', data, re.I)
        
        # Logic 2: Trace the Anomalous Routing (US -> UA -> BR)
        routing_hops = []
        if ".br" in data.lower(): routing_hops.append("Brazil (Compromised Relay)")
        if ".ua" in data.lower(): routing_hops.append("Ukraine (Attacker Node)")

        # --- AUDIT REPORT OUTPUT ---
        if len(auth_results) >= 3:
            print("[!] CRITICAL: Triple PASS detected. Technical filters bypassed.")
        
        if routing_hops:
            print(f"[!] TRACE FOUND: { ' -> '.join(routing_hops) }")
            print("[*] MITRE ATT&CK: T1566.002 (Spearphishing Link)")

    except FileNotFoundError:
        print(f"Error: Evidence file not found at {file_path}.")

# Execute Simulation using the file in your 'evidence' folder
run_forensic_simulation('evidence/evidence.eml')
