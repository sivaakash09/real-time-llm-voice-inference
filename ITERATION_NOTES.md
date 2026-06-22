# Iteration Notes

## Iteration 1: Improved identity-verification behavior

In the first test call, the patient simulator generally completed the conversation, but I noticed one issue: when the agent asked the patient to spell their first and last name and confirm date of birth, the simulator jumped ahead and gave the phone number instead.

Change made:
I updated the patient prompt so that when the agent asks for name, spelling, DOB, or phone number, the simulator answers exactly the requested field and does not skip ahead.

Why this matters:
The challenge evaluates lucid voice conversations first. This change made the caller more realistic and reduced avoidable confusion during verification-heavy flows.

## Iteration 2: Made new-patient intent clearer

In the first appointment scheduling call, the agent attempted to verify an existing patient record even though the goal was a new-patient appointment.

Change made:
I changed the opening line from:
“Hi, I wanted to schedule a new patient appointment.”

to:
“Hi, I’m a new patient and I wanted to schedule an appointment.”

Why this matters:
This makes the scenario clearer and helps distinguish whether the agent properly supports a new-patient scheduling flow.

# Iteration note:
# Added after early call review. The bot previously jumped ahead to phone number
# when the agent asked for spelling/DOB. These rules make it answer only the requested field.

# Iteration Notes ADDED after first call:

return f"""
...
Conversation rules:
- Speak like a normal patient.
...
- If the agent asks you to repeat or spell your name, spell your first and last name clearly.
- If the agent asks for date of birth, give only the date of birth.
- If the agent asks for phone number, give only the phone number.
- Answer exactly what the agent asks. Do not jump ahead to other information.
...
""".strip()