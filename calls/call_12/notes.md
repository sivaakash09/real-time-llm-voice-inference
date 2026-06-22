# Call 12 Notes

**Scenario:** `duplicate_appointment_question`  
**Goal:** Check whether the patient has one follow-up appointment or two.

## Bot Quality

Usable. The bot corrected the identity, provided DOB, gave the phone number, repeated the goal several times, and stayed focused on checking duplicate appointments.

## Agent Issue

The agent again started with the wrong identity: “Am I speaking with Priya?”

The agent repeatedly asked for phone number, full name, and date of birth, but did not answer whether there was one appointment or two. It also incorrectly used 510-588-5621 as the number on file before the caller corrected it.

## Decision

Keep this call. It is useful because it shows failure to resolve a duplicate appointment question after repeated verification.