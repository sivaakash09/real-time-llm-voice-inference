# Call 07 Notes

**Scenario:** `weekend_edge_case`  
**Goal:** Try to schedule an annual physical for Sunday at 10 AM.

## Bot Quality

Usable, but minor issue: the bot repeated “Okay, thanks for checking” twice.

The bot stayed on the weekend scheduling scenario and clearly requested Sunday at 10 AM.

## Agent Issue

The agent again started with the wrong identity: “Am I speaking with Priya?”

The agent said it could help and started checking availability, but did not explain whether Sunday was available or whether the office was closed. It transferred to a representative and the call ended.

## Decision

Keep this call as an edge-case scheduling test. It is not the strongest bug because the agent did not incorrectly confirm Sunday, but it still shows failure to resolve a weekend scheduling request.