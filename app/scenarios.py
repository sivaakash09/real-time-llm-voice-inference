SCENARIOS = {
    "appointment_basic": {
        "name": "Basic appointment scheduling",
        "patient_name": "Priya Shah",
        "goal": "Schedule a new patient appointment for recurring headaches.",
        "details": {
            "date_preference": "next Monday morning",
            "reason": "recurring headaches for the past two weeks",
            "insurance": "Aetna PPO",
            "dob": "April 12, 1997",
            "phone": "555-0198",
        },
        "opening_line": "Hi, I wanted to schedule a new patient appointment.",
        "behavior": "Be polite, clear, and cooperative.",
    },

    "reschedule_existing": {
        "name": "Reschedule existing appointment",
        "patient_name": "Marcus Lee",
        "goal": "Reschedule an existing appointment from Tuesday afternoon to Thursday morning.",
        "details": {
            "current_appointment": "Tuesday at 3 PM",
            "new_preference": "Thursday morning",
            "reason": "work conflict",
            "dob": "September 3, 1988",
            "phone": "555-0134",
        },
        "opening_line": "Hi, I need to reschedule an appointment I already have.",
        "behavior": "Answer identity questions normally. Confirm the new time if offered.",
    },

    "cancel_appointment": {
        "name": "Cancel appointment",
        "patient_name": "Anita Rao",
        "goal": "Cancel an appointment because symptoms improved.",
        "details": {
            "appointment": "Friday at 11 AM",
            "reason": "symptoms improved and patient no longer needs the visit",
            "dob": "January 22, 1995",
            "phone": "555-0181",
        },
        "opening_line": "Hi, I wanted to cancel my upcoming appointment.",
        "behavior": "Do not reschedule unless the agent strongly recommends it.",
    },

    "medication_refill": {
        "name": "Medication refill request",
        "patient_name": "Daniel Kim",
        "goal": "Ask for a refill for a medication and see whether the agent handles it safely.",
        "details": {
            "medication": "lisinopril",
            "supply_left": "two pills left",
            "pharmacy": "CVS on Greenbelt Road",
            "dob": "June 8, 1979",
            "phone": "555-0177",
        },
        "opening_line": "Hi, I’m calling because I need a medication refill.",
        "behavior": "Do not ask for medical advice. Just ask about the refill process.",
    },

    "office_hours_location": {
        "name": "Office hours and location",
        "patient_name": "Sophia Martin",
        "goal": "Ask about office hours, address, and parking.",
        "details": {
            "question_1": "office hours",
            "question_2": "exact location",
            "question_3": "parking availability",
            "dob": "March 15, 1992",
            "phone": "555-0109",
        },
        "opening_line": "Hi, I had a few questions about your office hours and location.",
        "behavior": "Ask follow-up questions if the answer is vague.",
    },

    "insurance_question": {
        "name": "Insurance coverage question",
        "patient_name": "Omar Hassan",
        "goal": "Ask whether the office accepts insurance before scheduling.",
        "details": {
            "insurance": "Blue Cross Blue Shield",
            "visit_type": "new patient primary care visit",
            "dob": "November 19, 1990",
            "phone": "555-0144",
        },
        "opening_line": "Hi, before I schedule, I wanted to check if you accept my insurance.",
        "behavior": "If the agent is unsure, ask what information they need to verify it.",
    },

    "weekend_edge_case": {
        "name": "Weekend scheduling edge case",
        "patient_name": "Emily Carter",
        "goal": "Try to schedule an appointment for Sunday at 10 AM.",
        "details": {
            "date_preference": "Sunday at 10 AM",
            "reason": "annual physical",
            "insurance": "UnitedHealthcare",
            "dob": "July 30, 1986",
            "phone": "555-0126",
        },
        "opening_line": "Hi, I wanted to see if I can come in this Sunday at 10 AM.",
        "behavior": "If the agent confirms Sunday without checking hours, accept naturally. This may reveal a bug.",
    },

    "unclear_request": {
        "name": "Unclear patient request",
        "patient_name": "Nina Patel",
        "goal": "Start with a vague request and see if the agent asks clarifying questions.",
        "details": {
            "vague_issue": "I need help with my medicine thing",
            "actual_need": "patient wants to know if they need an appointment for a refill",
            "dob": "May 5, 1998",
            "phone": "555-0166",
        },
        "opening_line": "Hi, I need help with my medicine thing.",
        "behavior": "Be vague at first. Clarify only if the agent asks good follow-up questions.",
    },

    "interruption_test": {
        "name": "Interruption and turn-taking test",
        "patient_name": "Robert Chen",
        "goal": "Test whether the agent handles a patient interrupting once during scheduling.",
        "details": {
            "reason": "lower back pain",
            "date_preference": "tomorrow afternoon",
            "insurance": "Cigna",
            "dob": "October 11, 1983",
            "phone": "555-0152",
        },
        "opening_line": "Hi, I need to schedule an appointment for back pain.",
        "behavior": "Interrupt once politely if the agent gives a long explanation. Say: Sorry, quick question — do you have anything tomorrow afternoon?",
    },

    "date_confusion": {
        "name": "Date confusion edge case",
        "patient_name": "Laura Johnson",
        "goal": "Test whether the agent clarifies an ambiguous date.",
        "details": {
            "ambiguous_date": "next Friday, but I am not sure of the exact date",
            "reason": "follow-up visit",
            "insurance": "Aetna",
            "dob": "December 2, 1991",
            "phone": "555-0115",
        },
        "opening_line": "Hi, I want to book a follow-up for next Friday, but I’m not sure what date that is.",
        "behavior": "See if the agent clarifies the actual date before confirming.",
    },
    "referral_question": {
    "name": "Referral requirement question",
    "patient_name": "Kevin Brooks",
    "goal": "Ask whether a referral is needed before scheduling a knee pain appointment.",
    "details": {
        "reason": "knee pain after running",
        "insurance": "Humana PPO",
        "dob": "February 14, 1985",
        "phone": "555-0192",
    },
    "opening_line": "Hi, I wanted to ask if I need a referral before scheduling for knee pain.",
    "behavior": "Ask whether you can schedule now or need to contact your primary care doctor first.",
},

"duplicate_appointment_question": {
    "name": "Possible duplicate appointment question",
    "patient_name": "Maya Singh",
    "goal": "Ask about a possible duplicate appointment notification.",
    "details": {
        "issue": "received two appointment reminder texts",
        "appointment_type": "follow-up visit",
        "dob": "August 9, 1993",
        "phone": "555-0188",
    },
    "opening_line": "Hi, I got two appointment reminder texts and wanted to check if I have duplicate appointments.",
    "behavior": "Ask the agent to confirm whether there is one appointment or two.",
},

"billing_question": {
    "name": "Billing question before visit",
    "patient_name": "Grace Miller",
    "goal": "Ask whether there is a copay or estimate before scheduling.",
    "details": {
        "insurance": "UnitedHealthcare",
        "visit_type": "new patient orthopedic visit",
        "dob": "April 4, 1989",
        "phone": "555-0172",
    },
    "opening_line": "Hi, before I schedule, I wanted to ask if you can tell me the copay or visit estimate.",
    "behavior": "If the agent cannot answer, ask who can help with billing questions.",
},
}


def get_scenario(scenario_id: str) -> dict:
    if scenario_id not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_id}")

    return SCENARIOS[scenario_id]


def build_patient_prompt(scenario: dict) -> str:
    detail_lines = "\n".join(
        f"- {key.replace('_', ' ').title()}: {value}"
        for key, value in scenario["details"].items()
    )

    return f"""
You are a realistic patient calling a medical office.

You are NOT an assistant.
You are the caller/patient.
Your job is to complete this scenario naturally.

Scenario name:
{scenario["name"]}

Patient name:
{scenario["patient_name"]}

Goal:
{scenario["goal"]}

Patient details:
{detail_lines}

Opening line:
{scenario["opening_line"]}

Behavior:
{scenario["behavior"]}

Conversation rules:
- Speak like a normal patient.
- Keep responses short, usually one sentence.
- Do not explain that you are an AI.
- Do not mention this is a test unless directly asked.
- Use only the fake patient details above.
- If the agent asks for information you do not have, say you are not sure.
- If the agent asks you to repeat or spell your name, spell your first and last name clearly. 
- If the agent asks whether they are speaking with a specific person, answer that identity question before anything else.
- Compare the name the agent says with the Patient name above. A first-name-only match counts as a match.
- If the name matches the Patient name, say: "Yes, this is {scenario["patient_name"]}."
- If the name does not match the Patient name, say: "No, this is {scenario["patient_name"]}."
- Do not give the opening line or scenario goal until any identity question is answered.
- If the agent asks for date of birth, give only the date of birth.
- If the agent asks for phone number, give only the phone number.
- Answer exactly what the agent asks. Do not jump ahead to other information.
- Stay focused on the scenario goal.
- Be polite and realistic.
""".strip()