# Bug Report

This report summarizes issues found while testing the Pretty Good AI clinic voice agent using simulated patient calls. Each bug includes the affected call transcript, recording, observed behavior, why it matters, and expected behavior.

---

## Bug 1: Agent gets stuck in identity verification and fails new-patient scheduling

**Severity:** Medium  
**Call:** `calls/call_01/transcript.txt`  
**Recording:** `calls/call_01/recording.mp3`

### Observed Behavior

The caller attempted to schedule a new-patient appointment for recurring headaches. The agent repeatedly asked for name, spelling, date of birth, and phone number. After it could not verify the phone number, it said it could not verify the record and offered to connect the caller to support.

When the caller clarified that they were a new patient and wanted an appointment, the agent still transferred the call. The appointment was not scheduled.

### Why This Matters

A new patient may not already have a verified record. The agent should recognize the new-patient path instead of blocking only on existing-patient verification.

### Expected Behavior

If the caller says they are a new patient, the agent should proceed with new-patient scheduling or clearly explain the next required step without abruptly ending the call.

---

## Bug 2: Agent uses stale patient identity and fails rescheduling workflow

**Severity:** Medium / High  
**Call:** `calls/call_02/transcript.txt`  
**Recording:** `calls/call_02/recording.mp3`

### Observed Behavior

The caller was Marcus Lee attempting to reschedule an existing appointment. However, the agent began by asking, “Am I speaking with Priya?” even though the current caller was Marcus.

After Marcus corrected the identity and provided date of birth, spelling, and phone number, the agent repeated verification steps and then said it could not proceed further. It transferred the call to support without handling the reschedule request.

### Why This Matters

The agent appears to carry over or infer the wrong patient identity from previous call context. This creates confusion and privacy risk in a healthcare scheduling flow. It also prevents the caller from completing a normal rescheduling task.

### Expected Behavior

The agent should verify the current caller independently, not assume a previous patient identity. Once the caller provides name, DOB, and phone number, the agent should proceed with rescheduling or clearly explain what information is missing.

---

## Bug 3: Wrong patient identity and incomplete refill capture

**Severity:** Medium / High  
**Call:** `calls/call_03/transcript.txt`  
**Recording:** `calls/call_03/recording.mp3`

### Observed Behavior

The caller was Daniel Kim requesting a lisinopril refill. The agent began by asking, “Am I speaking with Priya?” even though this was a different patient.

After the caller provided DOB, phone number, and said they had only two pills of lisinopril left, the agent said it would document the request. The caller then provided the pharmacy, CVS on Greenbelt Road, but the agent transferred the call without confirming whether the pharmacy information was captured.

### Why This Matters

Refill workflows need accurate patient identity and complete medication and pharmacy details. Carrying over a previous patient name and not confirming pharmacy can lead to an incomplete or unsafe request.

### Expected Behavior

The agent should verify the current caller independently and confirm medication, urgency, and pharmacy before documenting or transferring.

---

## Bug 4: Insurance verification flow loops and becomes too long

**Severity:** Medium  
**Call:** `calls/call_04/transcript.txt`  
**Recording:** `calls/call_04/recording.mp3`

### Observed Behavior

The caller asked whether the office accepts Blue Cross Blue Shield. The agent first asked, “Am I speaking with Priya?” even though this was a different patient.

The agent then sent an insurance upload link, but the flow looped several times. It repeatedly said the form was not submitted, asked the caller to retry, then repeated verbal insurance questions and “I’m processing that now.”

### Why This Matters

The patient gets stuck in a long repetitive flow instead of being moved quickly to verbal insurance collection or support follow-up.

### Expected Behavior

The agent should verify the current caller independently and exit the failed upload loop sooner.

---

## Bug 5: Wrong identity and phone number carryover

**Severity:** Medium  
**Call:** `calls/call_05/transcript.txt`  
**Recording:** `calls/call_05/recording.mp3`

### Observed Behavior

The caller was Sophia Martin asking about office hours, location, and parking. The agent first asked, “Am I speaking with Priya?” even though this was a different patient.

The agent also said the phone number on file was `510-588-5621`, which appears to be the caller ID or Twilio number, not the patient’s scenario phone number. The caller corrected it to `555-0109`.

### Why This Matters

The agent appears to carry over or infer the wrong identity and phone number across calls.

### Expected Behavior

The agent should verify the current caller independently and should not assume the previous patient identity or use caller ID as the patient phone number without confirmation.

---

## Bug 6: Agent fails to complete cancellation after verification

**Severity:** Medium  
**Call:** `calls/call_06/transcript.txt`  
**Recording:** `calls/call_06/recording.mp3`

### Observed Behavior

The caller wanted to cancel an upcoming appointment. The agent first asked, “Am I speaking with Priya?” even though this call used Anita Rao.

After the caller provided DOB, spelled the name, gave the phone number, and confirmed the details, the agent did not cancel the appointment. It repeated verification and transferred the call to a representative.

### Why This Matters

Appointment cancellation is a basic patient workflow. After verification, the agent should either complete the cancellation or clearly explain why it cannot.

### Expected Behavior

The agent should verify the caller, identify the appointment, confirm cancellation, and provide a clear cancellation outcome.

---

## Bug 7: Agent fails to resolve weekend scheduling request

**Severity:** Medium  
**Call:** `calls/call_07/transcript.txt`  
**Recording:** `calls/call_07/recording.mp3`

### Observed Behavior

The caller asked to schedule an annual physical for Sunday at 10 AM. The agent said it could help and began checking availability, but did not confirm availability, explain office hours, or say whether Sunday appointments are allowed. It then transferred the caller to a representative and the call ended.

### Why This Matters

Weekend scheduling is an important edge case. The agent should clearly tell the caller whether Sunday appointments are available or unavailable instead of silently transferring.

### Expected Behavior

The agent should check office hours and availability, then either offer a valid appointment time or explain that Sunday is unavailable and suggest a weekday alternative.

---

## Bug 8: Wrong identity at call start during successful scheduling

**Severity:** Medium  
**Call:** `calls/call_08/transcript.txt`  
**Recording:** `calls/call_08/recording.mp3`

### Observed Behavior

The caller was using the back-pain scheduling scenario, but the agent opened with “Am I speaking with Priya?” This wrong-identity pattern appeared across multiple calls with different patient names.

The rest of the call was mostly successful: the agent handled the interruption and booked the appointment.

### Why This Matters

Even in a successful scheduling flow, the wrong identity at the start suggests the agent may be carrying over patient context across calls.

### Expected Behavior

The agent should verify the current caller independently and should not assume the previous patient identity.

---

## Bug 9: Agent repeats verification and fails before handling scheduling request

**Severity:** Medium  
**Call:** `calls/call_10/transcript.txt`  
**Recording:** `calls/call_10/recording.mp3`

### Observed Behavior

The caller was Laura Johnson and intended to schedule a follow-up visit with an ambiguous date. The agent first asked, “Am I speaking with Priya?” even though this was a different patient.

After the caller provided DOB and spelled the full name, the agent repeated the same name/DOB verification request. It then confirmed the phone number and DOB but still said it could not proceed and transferred the caller to support.

### Why This Matters

The agent failed before reaching the actual scheduling task. Repeated verification and transfer prevents the patient from completing a basic appointment request.

### Expected Behavior

The agent should verify the caller once, then proceed to the scheduling request and clarify the ambiguous date.

---

## Bug 10: Agent uses wrong patient identity during referral question

**Severity:** Medium  
**Call:** `calls/call_11/transcript.txt`  
**Recording:** `calls/call_11/recording.mp3`

### Observed Behavior

The caller asked whether a referral was needed before scheduling for knee pain. The agent opened by asking, “Am I speaking with Priya?” even though this scenario used Kevin Brooks.

Later, the agent said there was already a knee pain appointment on file and could help reschedule or cancel it. At the end of the call, the agent said, “Thanks, Priya,” again using the wrong patient name.

### Why This Matters

The agent appears to carry over or infer the wrong patient identity across calls. In a healthcare workflow, wrong identity handling can confuse verification and create privacy risk.

### Expected Behavior

The agent should verify the current caller independently and should not reuse a previous patient name when handling a new scenario.

---

## Bug 11: Agent fails to answer duplicate appointment question after repeated verification

**Severity:** Medium / High  
**Call:** `calls/call_12/transcript.txt`  
**Recording:** `calls/call_12/recording.mp3`

### Observed Behavior

The caller was Maya Singh and asked whether she had one follow-up appointment or two because she received two reminder texts. The agent repeatedly asked for phone number, full name, and date of birth, but did not answer the appointment-count question.

The agent also used `510-588-5621` as the number on file before the caller corrected it to `555-0188`.

### Why This Matters

Duplicate appointment confusion is a common patient support issue. The agent should be able to verify the caller once and then clearly confirm whether there is one appointment or multiple appointments.

### Expected Behavior

The agent should verify the caller, check upcoming appointments, and clearly answer whether there is one appointment or two.

---

## Bug 12: Billing question transferred without clear handoff

**Severity:** Low / Medium  
**Call:** `calls/call_13/transcript.txt`  
**Recording:** `calls/call_13/recording.mp3`

### Observed Behavior

The caller asked whether the office could provide a copay or visit estimate before scheduling. The agent said it could not check an exact estimate and offered to note the billing question for support.

When the caller asked who could help with billing questions, the agent immediately transferred to a representative. It did not explain who would help, what information would be documented, or what the caller should expect next.

### Why This Matters

Billing questions are common before scheduling. A clearer handoff would reduce confusion.

### Expected Behavior

The agent should explain that clinic support or billing staff will follow up, confirm the caller’s question, and then transfer or create a support case.

---

## Note on Call 09

`calls/call_09/transcript.txt` and `calls/call_09/recording.mp3` were a duplicate interruption-test call. I kept the artifacts as an extra call attempt but did not create a separate bug entry because the transcript duplicated Call 08.

---

## Overall Recurring Issue

Across many calls, the agent repeatedly opened with “Am I speaking with Priya?” even when the scenario patient was Marcus Lee, Daniel Kim, Sophia Martin, Anita Rao, Emily Carter, Kevin Brooks, Maya Singh, or another caller. The agent also sometimes used the Twilio caller ID as the patient phone number.

This suggests a broader context or identity-handling issue. In a healthcare setting, identity verification must be isolated per call and should not reuse stale names or phone numbers from earlier interactions.