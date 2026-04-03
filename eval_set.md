# Evaluation Set

## Case 1: Normal Case

Input:
Customer: John Smith, ABC Corp
Context: Product demo for CRM software
Key Points: automation features, pricing, next meeting

Good Output Should:

- be professional and polite
- summarize the demo
- mention key features
- propose next steps

---

## Case 2: Missing Information (Edge Case)

Input:
Customer: Unknown
Context: meeting happened
Key Points:

Good Output Should:

- avoid making up details
- stay generic but coherent
- suggest follow-up

---

## Case 3: Likely Failure Case

Input:
Customer: Sarah
Context: unclear notes
Key Points: random incomplete phrases

Good Output Should:

- avoid hallucination
- remain cautious
- possibly indicate uncertainty

---

## Case 4: Detailed Enterprise Follow-Up

Input:
Customer: Priya Nair, Horizon Health
Context: second meeting after enterprise platform demo
Key Points: security review, SSO integration, annual contract option, requested pricing sheet by Friday

Good Output Should:

- reflect a professional B2B tone
- mention the major discussion points clearly
- include a concrete next step tied to the pricing sheet
- avoid adding technical claims not present in the notes

---

## Case 5: Ambiguous Next Step

Input:
Customer: Miguel, small retail business
Context: short discovery call
Key Points: interested in automation, asked about budget, timeline maybe next month

Good Output Should:

- stay helpful even though the notes are incomplete
- mention interest in automation and budget carefully
- suggest a soft next step instead of pretending a meeting is already booked
- remain concise and realistic
