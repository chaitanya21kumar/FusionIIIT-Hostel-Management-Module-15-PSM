# HM-UC-026 — Visitor Entry Management

## Primary Actor
Visitor, Gate Security

## Stakeholders
- Hostel Management
- Students
- Security Team

## Preconditions
- Visitor arrives at hostel gate
- Gate security is logged in

## Trigger
Visitor wants to enter the hostel

## Main Success Scenario
1. Visitor provides details at the gate
2. Gate Security enters details in VisitorEntryForm
3. System validates visitor
4. System creates VisitRequest
5. Visitor is allowed entry

## Alternate Flows
A1. Invalid details → entry denied  
A2. Visitor already has an active request → reuse existing  

## Postconditions
- VisitRequest created
- Visitor entry recorded

## Business Rules
BR-HM-030 Valid visitor information required  
BR-HM-031 One active visit per visitor  

## Entities
Visitor, VisitRequest

## Boundaries
VisitorEntryForm, GateSecurityView

## Controls
VisitorController
