# TryHackMe: Nmap Room Walkthrough

**Date:** February 2026  
**Room Link:** https://tryhackme.com/room/furthernmap  
**Difficulty:** Beginner  

**Objective:** Learn basic network enumeration with Nmap.

**Tools Used:** Kali Linux, nmap

**Steps:**
1. Started VM → Noted target IP: 10.10.x.x
2. Basic scan: `nmap -sV 10.10.x.x`  
   Output: Discovered ports 22 (SSH), 80 (HTTP), service versions.
3. Aggressive scan: `nmap -A 10.10.x.x` → Found OS guess, scripts ran.
4. Vulnerability scan: `nmap --script vuln 10.10.x.x`

**Key Takeaways:**
- Service/version detection helps identify exploits.
- Always use -sV/-A for thorough recon.
- Ethical note: Only scan authorized targets.

**Screenshot:** ![nmap-output](nmap-screenshot.png)  <!-- Upload image to repo -->