# WF-108 — Step-4 Change Log
Workflow: HM-WF-108 — Visitor & Access Management  
Use Cases: HM-UC-026, HM-UC-027, HM-UC-028  

This log records all changes introduced while realizing the full
workflow on top of the Step-3 domain model.

---

## Workflow Nodes
The Visitor Management workflow consists of:

1. Submit Visitor Request  
2. Validate Visitor  
3. Approve or Reject Request  
4. Allow Visitor Entry  
5. Record Visitor Exit  

---

## New Control Classes (from Workflow)

| Class | Reason |
|------|--------|
| VisitWorkflowController | Orchestrates end-to-end visitor workflow |
| AccessMonitoringService | Coordinates visitor presence and exit tracking |

---

## New Operations Added

### VisitWorkflowController
- submitVisit()
- approveVisit()
- rejectVisit()
- closeVisit()

### AccessMonitoringService
- trackActiveVisits()
- validateExit()

---

## Updated Associations

| From | To | Meaning |
|------|----|--------|
| VisitWorkflowController | VisitRequest | Controls lifecycle |
| VisitWorkflowController | VisitorController | Initiates requests |
| VisitWorkflowController | ApprovalController | Triggers approvals |
| VisitWorkflowController | ExitController | Triggers exit closure |
| AccessMonitoringService | VisitLog | Monitors exits |
| AccessMonitoringService | VisitRequest | Tracks active visitors |

---

## Summary
After Step-4, WF-108 is fully realized:
- UC behavior (Step-2)
- State lifecycle (Step-3)
- Workflow orchestration (Step-4)

This model is the **final PIM** of the Visitor Management system.
