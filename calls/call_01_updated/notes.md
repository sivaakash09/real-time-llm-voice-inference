# Call 01 updated Notes

Scenario: appointment_basic  
Patient: Priya Shah  
Outcome: Agent verified the patient and attempted scheduling, but blocked the request due to an existing appointment of the same visit type.

Bot quality:
- Improved from call_01.
- The bot answered name/DOB questions directly.
- Turn-taking was coherent.

Agent issue:
- The agent reported an existing appointment and refused to book another new patient appointment.
- This may indicate stale state or incorrect duplicate appointment detection, unless a previous appointment was actually created in the test environment.