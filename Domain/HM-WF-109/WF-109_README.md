WF-109 – Room Vacation Workflow

This document summarizes what has been completed so far for Workflow 109.

Use Cases Covered
HM-UC-029 – Request Room Vacation
HM-UC-030 – Verify Clearance Requirements
HM-UC-031 – Complete Room Vacation

Current Status
Step 1 (Use Case to EBC) has been completed.

The following has been produced:
• Separate EBC diagrams for UC-029, UC-030 and UC-031
• A merged EBC diagram for WF-109 combining all three use cases
• All classes are categorized as Entity, Boundary or Control
• All attributes and relationships are derived directly from the use case descriptions

Entities Identified
Student
RoomVacationRequest
ClearanceChecklist
RoomInspection
ClearanceCertificate
Room
StudentHostelRecord
VacationCompletionReport

Boundaries Identified
RoomVacationForm
ClearanceVerificationView
VacationFinalizationView

Controls Identified
VacationRequestController
ClearanceController
VacationFinalizationController

What is not done yet
Step 2 – Sequence diagrams and behavioral updates
Step 3 – State diagram for RoomVacationRequest
Step 4 – Workflow realization and final PIM

Next Step
The next activity is Step 2, where sequence diagrams will be created for UC‑029, UC‑030 and UC‑031 and the domain model will be updated with discovered operations and associations.
