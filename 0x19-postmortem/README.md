#0x19-postmortem

Postmortem: Web Stack Outage - 2024-02-10

Issue Summary:

Duration:
Start Time: 2024-02-10, 14:30 WAT
End Time: 2024-02-10, 17:45 WAT

Impact:
Hold onto your keyboards! The user authentication service took an unscheduled siesta, leaving 30% of users locked out. Users experienced login fails and were stranded in the digital wilderness.

Timeline:

Detection:
Detected at 14:30 WAT through monitoring alerts indicating a spike in authentication errors.
Actions Taken:
1. Investigated backend services, initially focusing on recent code deployments.
2. Assumed a potential database issue, leading to further examination of database connections and queries.

Misleading Paths:
1. Initial focus on recent code deployments was misleading, as the issue was not related to recent changes.
2. Assumption of a database issue delayed identification of the actual root cause.

Escalation:
Escalated to the DevOps and Database teams at 15:15 WAT for deeper investigation.

Resolution:
1. Identified a misconfiguration in the authentication service that caused incorrect validation of user credentials.
2. Applied a hotfix to the configuration at 17:30 WAT, resolving the issue and restoring normal service.

ROOT CAUSE AND RESOLUTION 
Root Cause:
The misconfiguration in the authentication service prevented proper validation of user credentials, leading to authentication failures.

Resolution:
Applied a hotfix to the authentication service configuration, correcting the misconfiguration and restoring proper functionality.

CORRECTIVE AND PREVENTIVE MEASURES

Improvements/Fixes:
1. Implement a more robust monitoring system for early detection of misconfigurations and authentication failures.
2. Enhance the deployment process to include thorough testing of critical services after updates.
3. Conduct a comprehensive review of configuration management practices to prevent similar misconfigurations in the future.

Tasks:
1. Update monitoring alerts to include specific triggers for authentication-related issues.
2. Conduct a post-incident review with the development and operations teams to share lessons learned and improve incident response.
3. Implement automated testing for critical configuration files to catch misconfigurations before deployment.
4. Schedule a security audit for all critical services to identify and address potential vulnerabilities.

This postmortem outlines the key details of the recent web stack outage. The incident's impact on user authentication and the subsequent actions, along with a detailed timeline, provide a clear understanding of the situation. The root cause was traced to a misconfiguration in the authentication service, which was promptly resolved with a hotfix. Moving forward, corrective and preventative measures have been outlined to avoid similar incidents, including improvements in monitoring, testing, and configuration management practices.

