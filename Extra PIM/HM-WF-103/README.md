Hostel Management Workflow — Requirements Modeling
Module
Hostel Management Module — Student Onboarding & Room Allotment

Version
v1.0 — Complete PIM Workflow Modeling Deliverable

Workflow ID
HM-WF-103 — New Student Room Allotment & Onboarding Workflow

(Covers Use Cases: HM-UC-012, HM-UC-013, HM-UC-014)

Objective
To model the complete end-to-end process of new student placement—from bulk room allocation and capacity validation to automated onboarding notifications and audit-logged room change reviews.

Tools Used
Modeling: Mermaid & XML (EBC class diagrams, sequence diagrams, state machine, activity workflow)

Documentation: Markdown (.md) (UC annotations, tables, workflow realization, completeness, change logs)

Submission: Canvas / Academic Portal

Deliverables Summary
Step 1 — Requirements & Structural Modeling
Use Case Annotations: Boundary–Control–Entity mapping for HM-UC-012 (Notify), HM-UC-013 (Bulk Allotment), and HM-UC-014 (Room Change).

PIM Class Tables: Defining core attributes for Room, AccommodationRequest, AllotmentRecord, and HostelPolicy.

Initial EBC Class Diagrams: Visualizing structural links between the Admin bulk-actions portal and the student onboarding gateway.

Step 2 — Interaction Modeling
Sequence Diagram (HM-UC-013): Modeling the bulk allotment logic including capacity gatekeeping and transaction rollback.

Sequence Diagram (HM-UC-012): Automated student notification and profile update loop post-assignment.

Update Log: Documentation of logic refinements, specifically separating the CapacityCheckController from the AllotmentEngine.

Step 3 — Behavioral Modeling
State Machine Diagram: Room Occupancy lifecycle (Available → Partially Occupied → Full → Maintenance/Locked).

Lifecycle-aligned EBC: Integrating the SystemAuditLogController and PolicyValidationController to manage the "Approved/Rejected" transitions.

Step 4 — Workflow Realization
Completeness Verification: Mapping actors (Student, Super Admin, Warden), activity nodes (N1 through N7), and Business Rules (BR-HM-111 through BR-HM-114).

Workflow Realization Map: Tracing logical paths from bulk submission to successful onboarding (END-1) or capacity-driven failure (END-2, END-3).

Final Stable EBC Model: The consolidated architectural view of the Room Allotment system.

Modeling Scope
Actors: Student, Super Admin, Caretaker, Warden.

Core Domain: Room Entities, Bulk Assignment Transactions, Onboarding Notifications, Policy Audit Logs.

Focus: High-throughput transactional integrity and strict separation of Boundary (UI), Control (Logic), and Entity (Data) layers.

PIM Standards: Platform-neutral modeling ensuring scalability for both web and mobile administrative clients.