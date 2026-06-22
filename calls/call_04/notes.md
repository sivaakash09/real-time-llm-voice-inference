# Call 04 Notes

**Scenario:** `insurance_question`  
**Goal:** Check insurance before scheduling.

## Bot Quality

Usable, but the call was too long. The bot followed the insurance scenario, but stayed in the upload-link loop too long.

## Agent Issue

The agent again started with the wrong identity: “Am I speaking with Priya?”

The insurance upload flow became repetitive. The agent said the form was not submitted multiple times, asked the caller to retry, then repeated insurance questions and “I’m processing that now.”

## Decision

Keep as an extra bug/edge-case call. Do not use as one of the strongest final calls unless needed because it ran about 7 minutes.