---
title: Week in Review — LLM-Generated Code Not Secure, Africa Under Attack
date: 2025-08-02 09:00
category: Week in Review
tags: Dark Reading, Africa, cybersecurity, articles, cyberattacks
featured_image: images/2025-08-02-digital-credentials-online-shutterstock.jpg
image_caption: Source — 3rdtimeluckystudio via Shutterstock
---

A Veracode study of over 100 large language models (LLMs) across 80 coding tasks found [only about 55% of AI‑generated 
code passed security scans](https://www.darkreading.com/application-security/llms-ai-generated-code-wildly-insecure) —
even though over 90% now compile without error. Java was especially problematic, with a 
vulnerability rate above 45%, while developers also encountered frequent issues like slopsquatting — LLMs hallucinating 
nonexistent libraries—and susceptibility to prompt injection. The report warns against “vibe coding,” where developers 
rely on AI without embedding security requirements, urging organizations to integrate security checks, remediation 
tools, and developer training into AI‑driven workflows to avoid accumulating long‑term security debt.

A security researcher found that Azure Logic Apps’ API Connections [sometimes permitted users with read‑only or 
unauthenticated privileges to access sensitive data](https://www.darkreading.com/vulnerabilities-threats/low-code-tools-azure-allowed-unprivileged-access) 
across other applications and infrastructure components. The vulnerability arises 
because while Azure Resource Management (ARM) properly restricts low‑privilege users to GET requests, the underlying 
API Connection objects do not consistently honor those restrictions, enabling broader access than intended.
The issue was discovered by Binary Security’s Haakon Gulbrandsrud and will be detailed at Black Hat USA; 
Microsoft has since patched the flaw, but the finding emphasizes the need for explicit oversight of auto-generated 
API Connections in low-code Azure deployments.

Starting July 22, multiple African organizations including South Africa’s National Treasury, local government entities, 
universities, and private firms were [compromised through widespread exploitation of four related on-premises SharePoint 
vulnerabilities](https://www.darkreading.com/cyber-risk/african-orgs-mass-microsoft-sharepoint-exploits) dubbed 
"ToolShell." While initial targeting was likely by China-linked cyberespionage groups, later 
attacks became opportunistic—scanning exposed SharePoint servers indiscriminately across Africa and beyond, exploiting 
systems before patches were applied. The incident underscores Africa’s expanding digital infrastructure and reliance on 
on‑premises software, emphasizing urgent needs for layered defenses, rapid patching, vulnerability management, and 
better monitoring to prevent future mass intrusions.