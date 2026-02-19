# Basic Threat Model: Hypothetical Web App

**Asset:** User login system  
**Threat Actors:** External attackers  
**Using MITRE ATT&CK:** Initial Access (T1190 Exploit Public-Facing App)  
**Mitigations (NIST CSF):** PR.AC-1 Identity Management, DE.CM-1 Network Monitoring  
**Findings:** Recommend JWT + rate limiting to reduce brute-force risk.