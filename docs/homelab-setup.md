# Personal Kali Linux Home Lab Setup

**Goal:** Safe environment for testing tools and hardening practice.

**Setup Steps (VirtualBox/VMware):**
1. Download Kali ISO: https://www.kali.org/get-kali/
2. Create VM: 4GB RAM, 2 CPUs, 60GB disk.
3. Install → Update: `sudo apt update && sudo apt upgrade -y`
4. Basic hardening:
   - Change default password: `passwd`
   - Disable root login in SSH: Edit /etc/ssh/sshd_config → PermitRootLogin no → `sudo systemctl restart ssh`
   - Firewall: `sudo ufw enable` & allow SSH: `sudo ufw allow 22`
5. Installed tools: `sudo apt install nmap wireshark burpsuite`

**Before/After Comparison:**
- Before: Default open ports/services.
- After: Reduced attack surface, logged changes.

**Next Steps:** Add pfSense VM for network segmentation.