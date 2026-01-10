# Hostel Management (HM) Domain Model - PIM-lite

**Module:**Management (HM)
**Workflow ID:** HM-WF-113
**Workflow Name:** Extended Stay During Vacations Management

---

## Workflow Scope
**Description:** This workflow covers the lifecycle of a student requesting to stay in the hostel during vacation periods, including faculty authorization verification, charge calculation, payment tracking, service coordination (mess/security), and violation monitoring.

**Included Use Cases:**
* [cite_start]**HM-UC-038:** Apply for Extended Stay [cite: 167]
* [cite_start]**HM-UC-039:** Review and Approve Application [cite: 169]
* [cite_start]**HM-UC-040:** Manage Extended Stay Operations [cite: 171]

**Key Business Rules:**
* [cite_start]**Eligibility & Validation:** BR-HM-061 (Eligibility), BR-HM-062 (Vacation Dates), BR-HM-063 (Authorization Docs) [cite: 257, 259, 261]
* [cite_start]**Financial:** BR-HM-064 (Charge Calc), BR-HM-073 (Payment Deadlines) [cite: 263, 283]
* [cite_start]**Operations:** BR-HM-067 (Capacity), BR-HM-074 (Services), BR-HM-076 (Violations) [cite: 269, 285]

---

## Folder Structure
* **step1_uc_annotations/**: Annotated Use Case text.
* **step1_tables/**: Tabular extraction of classes.
* **step1_diagrams/**: Initial EBC diagrams.
* **step2_sequences/**: Sequence diagram for Anchor UC (HM-UC-038).
* **step2_diagrams/**: Updated Domain Model (post-sequence).
* **step3_states/**: State Machine for `ExtendedStayApplication`.
* **step3_diagrams/**: Updated Domain Model (post-state).
* **step4_workflow/**: Workflow realization map and completeness report.
* **step4_diagrams/**: Final PIM-lite domain model.