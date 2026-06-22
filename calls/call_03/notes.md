# Call 03 Notes

**Scenario:** `medication_refill`  
**Patient:** Daniel Kim  
**Goal:** Request a lisinopril refill with two pills left.

## Bot Quality

Usable. The bot stayed on the refill scenario, provided DOB, phone number, medication name, urgency, and pharmacy.

Minor issue: the transcript rendered the name as “Danielle Kim” instead of “Daniel Kim,” likely due to pronunciation/transcription.

## Agent Issue

The agent started by asking, “Am I speaking with Priya?” even though this call used Daniel Kim. This suggests possible stale identity carryover from a previous call.

The agent also said it would document the refill request before confirming the pharmacy. When the caller provided CVS on Greenbelt Road, the agent transferred without confirming that the pharmacy was captured.

## Decision

Keep this call. It is useful for testing medication refill handling and identity carryover.