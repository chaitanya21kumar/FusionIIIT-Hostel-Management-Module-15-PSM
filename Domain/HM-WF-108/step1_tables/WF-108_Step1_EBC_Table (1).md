# WF-108 — STEP-1 EBC TABLE

## Legend
- **<<Entity>>** — Business objects with persistent state  
- **<<Boundary>>** — Screens, forms, views, UI actions  
- **<<Control>>** — Coordinators, validators, transaction logic  

## STEP-1: Extracted EBC Classes

| Class Name | Stereotype | Attributes (from UC text only) | Methods (from UC text) | UC IDs |
|------------|------------|--------------------------------|------------------------|--------|
| Visitor | <<Entity>> | name, phone | — | HM-UC-026 |
| VisitRequest | <<Entity>> | requestID, visitDate, status | — | HM-UC-026, HM-UC-027, HM-UC-028 |
| VisitLog | <<Entity>> | logID, entryTime, exitTime | — | HM-UC-028 |
| VisitorEntryForm | <<Boundary>> | — | enterVisitorDetails(), submitRequest() | HM-UC-026 |
| GateSecurityView | <<Boundary>> | — | — | HM-UC-026 |
| WardenApprovalView | <<Boundary>> | — | viewPendingRequests(), approveRequest(), rejectRequest() | HM-UC-027 |
| ExitLogView | <<Boundary>> | — | recordExit() | HM-UC-028 |
| VisitorController | <<Control>> | — | validateVisitor(), createVisitRequest() | HM-UC-026 |
| ApprovalController | <<Control>> | — | approveVisit(), rejectVisit() | HM-UC-027 |
| ExitController | <<Control>> | — | closeVisit() | HM-UC-028 |

## STEP-1: Class Relationship Data

| From | Relationship | To | Evidence from UC |
|------|-------------|----|----------------|
| Visitor | creates | VisitRequest | UC-026 |
| VisitorEntryForm | uses | VisitorController | UC-026 |
| GateSecurityView | uses | VisitorController | UC-026 |
| WardenApprovalView | uses | ApprovalController | UC-027 |
| ApprovalController | updates | VisitRequest | UC-027 |
| ExitLogView | uses | ExitController | UC-028 |
| ExitController | updates | VisitRequest | UC-028 |
| ExitController | creates | VisitLog | UC-028 |
