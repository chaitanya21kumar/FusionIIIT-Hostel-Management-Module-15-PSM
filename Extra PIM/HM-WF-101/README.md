Hostel Management Workflow — Requirements Modeling
Module
Hostel Management Module — Student Leave Management

Version
v1.0 — Complete PIM Workflow Modeling Deliverable

Workflow ID
HM-WF-001 — Student Leave Request Workflow (Covers Use Cases: HM-UC-001, HM-UC-002, HM-UC-003, HM-UC-004)

Objective
To model the complete end-to-end process of student leave—from initial submission and document upload to review by the Caretaker, decision notification, and automated attendance synchronization.

Tools Used
Modeling: Mermaid (EBC class diagrams, sequence diagrams, state machine, activity workflow)

Documentation: Markdown (.md) (UC annotations, tables, workflow realization, completeness, change logs)

Submission: Canvas / Academic Portal

Deliverables Summary
Step 1 — Requirements & Structural Modeling
Use Case Annotations: Boundary–Control–Entity mapping for HM-UC-001 through HM-UC-004.

PIM Class Tables: Defining attributes for LeaveRequest, SupportingDocument, and AttendanceRecord.

Initial EBC Class Diagrams: Visualizing structural links for Leave Request submission and processing.

Step 2 — Interaction Modeling
Sequence Diagram (HM-UC-001): Submit Leave Request including validation and document handling.

Sequence Diagram (HM-UC-002): Process Leave Request showing caretaker decision logic.

Sequence Diagram (HM-UC-004): Automated attendance updates and notifications.

Update Log: Refining controller separation (Validation vs. Decision vs. AttendanceSync).

Step 3 — Behavioral Modeling
State Machine Diagram: LeaveRequest lifecycle (Draft → Pending → Approved/Rejected → Archived).

Lifecycle-aligned EBC: Integrating the LeaveArchiveController and SystemAuditLogController.

Step 4 — Workflow Realization
Completeness Verification: Mapping actors, nodes, and BR-HM-101 through BR-HM-105.

Workflow Realization Map: Tracing use cases to workflow end states (END-1, END-2).

Final Stable EBC Model: The consolidated architectural view of the Leave Management system.

Modeling Scope
Actors: Student, Caretaker, System.

Core Domain: Leave Request, Supporting Documents, Attendance Synchronization, Audit Logs.

Focus: Strict separation of Boundary (UI), Control (Logic), and Entity (Data) layers.

PIM Standards: Platform-neutral modeling (no database or language-specific logic).

Outcome
This PIM provides a traceable and interaction-validated design for Student Leave Management. It ensures that every step—from validation of mandatory documents to the final update of security gate-pass status—is handled by a dedicated component.

Status
✔ Workflow fully realized ✔ All use cases (HM-UC-001 to 004) covered ✔ All business rules (BR-HM-101 to 105) enforced ✔ PIM declared final and stable