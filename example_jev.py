"""Example 4: Jev (System One) evaluation - structured answers, no text."""
from deharness import evaluate

r = evaluate(
    model="jev-1.13-free",
    state="My order arrived late and the item is damaged. I want a refund.",
    questions={
        "department": {
            "type": "choice",
            "instructions": "Which team should handle this request?",
            "criteria": {
                "returns": "Refunds, exchanges, or damaged items",
                "shipping": "Delivery delays or lost packages",
                "billing": "Charges, invoices, or payment problems",
            },
        },
        "frustration": {
            "type": "score",
            "instructions": "How frustrated is the customer?",
            "criteria": ["Calm", "Frustrated", "Very angry"],
        },
    },
)
print(r["status"], r["answers"], r["usage"])
assert r["status"] == 200
