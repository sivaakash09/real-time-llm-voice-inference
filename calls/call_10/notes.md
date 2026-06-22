# Call 10 Notes

**Scenario:** `date_confusion`  
**Goal:** Schedule a follow-up for “next Friday” and test whether the agent clarifies the date.

## Bot Quality

Usable. The bot corrected the identity, provided DOB, spelled the name clearly, and repeated the requested information when asked.

## Agent Issue

The agent again started with the wrong identity: “Am I speaking with Priya?”

The agent repeated the same name/DOB verification request twice. After confirming the phone number and DOB, it said it could not proceed and transferred to support. The scheduling/date-confusion scenario was never handled.

## Decision

Keep this call as a verification failure call. It is not a strong date-confusion test because the agent never reached the scheduling request.