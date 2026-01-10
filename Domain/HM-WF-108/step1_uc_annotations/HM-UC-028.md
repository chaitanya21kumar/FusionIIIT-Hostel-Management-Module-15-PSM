# HM-UC-028 — Visitor Exit Logging

## Primary Actor
Gate Security

## Stakeholders
- Hostel Management
- Students
- Security

## Preconditions
- Visitor has an active VisitRequest

## Trigger
Visitor leaves hostel

## Main Success Scenario
1. Gate Security opens ExitLogView
2. Gate Security selects visitor
3. System closes VisitRequest
4. System creates VisitLog

## Alternate Flows
A1. No active visit → error shown  

## Postconditions
- VisitLog created
- VisitRequest closed

## Business Rules
BR-HM-034 Exit must be logged  
BR-HM-035 Only active visits can be closed  

## Entities
VisitRequest, VisitLog

## Boundaries
ExitLogView

## Controls
ExitController
