# HM-UC-027 — Visitor Approval

## Primary Actor
Warden

## Stakeholders
- Hostel Management
- Students
- Security

## Preconditions
- VisitRequest exists
- Warden is authenticated

## Trigger
Warden reviews pending visitor requests

## Main Success Scenario
1. Warden opens WardenApprovalView
2. System shows pending VisitRequests
3. Warden approves or rejects request
4. System updates VisitRequest status

## Alternate Flows
A1. Request rejected → status updated to Rejected  

## Postconditions
- VisitRequest marked Approved or Rejected

## Business Rules
BR-HM-032 Only warden can approve  
BR-HM-033 Approved visitors only may stay  

## Entities
VisitRequest

## Boundaries
WardenApprovalView

## Controls
ApprovalController
