WF-108 — Visitor & Access Management

Module: Hostel Management (HM)
Workflow ID: HM-WF-108
Use Cases: HM-UC-026, HM-UC-027, HM-UC-028

1. Purpose of this Workflow

WF-108 manages the complete lifecycle of a hostel visitor:
from entry request, through warden approval, to exit logging.

It ensures that:

Only valid visitors are registered

Only approved visitors are allowed to stay

Every exit is properly logged

This workflow integrates security, administration, and auditability.

2. Use Cases Covered
Use Case	Name
HM-UC-026	Visitor Entry Management
HM-UC-027	Visitor Approval
HM-UC-028	Visitor Exit Logging
3. Modeling Methodology Used

This workflow was designed using the mandated 4-step method:

Use Case → EBC extraction

Sequence Diagrams → Behavioral discovery

State Model → Stateful entity refinement

Workflow Realization → Final PIM

This ensures:

Full traceability

Policy enforcement

Workflow-driven domain design

4. Central Stateful Entity

The core business object is:

VisitRequest

It models the full visitor lifecycle.

States

Pending → Approved → Closed
        ↘ Rejected


Attributes

requestID

visitDate

status

submittedAt

approvedAt

rejectedAt

closedAt

State-driven operations

setPending()

approve()

reject()

close()

5. Final Domain Architecture
Entities

Visitor

VisitRequest

VisitLog

Boundaries

VisitorEntryForm

GateSecurityView

WardenApprovalView

ExitLogView

Controls

VisitorController

ApprovalController

ExitController

VisitWorkflowController (workflow orchestration)

AccessMonitoringService (runtime tracking)

6. Workflow Realization

The workflow is realized through the following orchestration:

Workflow Step	Model Operation
Submit visitor	VisitWorkflowController.submitVisit()
Validate visitor	VisitorController.validateVisitor()
Create visit	VisitRequest.create(), setPending()
Approve / Reject	VisitWorkflowController.approveVisit(), rejectVisit()
Apply decision	VisitRequest.approve(), reject()
Allow entry	GateSecurityView → AccessMonitoringService
Monitor visits	AccessMonitoringService.trackActiveVisits()
Close visit	ExitController.closeVisit()
Log exit	VisitLog.createLog()
7. Business Rule Enforcement
Rule	Enforcement
BR-HM-030 Valid visitor required	VisitorController.validateVisitor()
BR-HM-031 One active visit per visitor	VisitRequest.setPending()
BR-HM-032 Only warden can approve	ApprovalController.processDecision()
BR-HM-033 Only approved visitors stay	VisitRequest.approve()
BR-HM-034 Exit must be logged	VisitLog.createLog()
BR-HM-035 Only active visits can close	VisitRequest.close()
8. What This Workflow Guarantees

No unapproved visitor can remain inside the hostel

No visitor can leave without being logged

Every visit is auditable

All security and administrative actions are traceable to a model element

9. Status

WF-108 is fully completed with:

UC annotations

Step-1 EBC

Step-2 sequences

Step-3 state model

Step-4 final PIM

Completeness report

Workflow realization map

This workflow is ready for submission and grading.