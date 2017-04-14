# PSAttack
* Author: illwill
* Version: Version 0.1
* Target: Windows with .NET 4.0

## Description

Opens powershell with UAC bypass, waits for webserver to start, determines if target is 32 or 64 bit, then downloads PSAttack .csproj file onto the target and compiles it within MSBuild using 'Inline Tasks' to bypass Application Whitelisting and Device Guard

PSAttack from https://github.com/jaredhaight/psattack

MSBuild Inline Task bypass from @subtee http://subt0x10.blogspot.nl/2016/09/bypassing-application-whitelisting.html

PSA x32 & x64 .csproj files from Nicky Tyrer https://gist.github.com/NickTyrer/8389c3d5698511f5c81bc472ee49a11c

PSAttack Tools:
* FuzzySecurity - Invoke-MS16-032
* PowerSploit - Invoke-Shellcode
* PowerSploit - Invoke-Mimikatz
* PowerSploit - Invoke-GPPPassword
* PowerSploit - Invoke-Ninjacopy
* PowerSploit - Invoke-WMICommand
* PowerSploit - VolumeShadowCopyTools
* Putterpanda - Invoke-Mimikittenz
* Kevin Robinson - Tater
* Kevin Robertson - Inveigh
* Kevin Robertson - Inveigh-Relay
* Nishang - Gupt-Backdoor
* Nishang - Get-Information
* Nishang - Do-Exfiltration
* Nishang - Get-Wlan-Keys
* Nishang - Out-Dnstxt
* Nishang - dns_txt_pwnage
* Nishang - Invoke-PsUACme
* Nishang - Add-Exfiltration
* Besimorhino - Powercat
* PowerTools - PowerUp
* PowerTools - PowerView
* Jared Haight - Invoke-MetasploitPayload
* Jared Haight - New-ScheduledTaskZ
* PSAttack - Get-Attack

## Configuration

None needed. 

## STATUS

| LED                            | Status                                                              |
| ------------------------------ | ------------------------------------------------------------------- |
| Stage 1 (Yellow single blink)  | Running Powershell with UAC Bypass / Waiting for WebServer to start |
| BLUE (Blinking)                | Waiting for WebServer to start                                      |
| Stage 2 (Yellow double blink)  | Webserver Started                                                   |
| Magenta(Blinking fast)         | Downloading PSAttack                                                |
| Green(Blinking)                | PSAttack running                                                    |

## Discussion
[Hak5 Forum Thread](https://forums.hak5.org/index.php?/topic/40761-payload-psattack/ "Hak5 Forum Thread")
