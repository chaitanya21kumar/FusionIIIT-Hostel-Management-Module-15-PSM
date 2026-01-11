# HM-UC-024 — Manage Guard Shift Schedules

## Primary Actor
Security Supervisor

## Stakeholders
- Students (safety)
- Hostel Administration
- Security Guards

## Preconditions
- Supervisor is authenticated
- Guards exist in the system

## Trigger
Supervisor wants to create or update guard shifts

## Main Success Scenario
1. Supervisor opens GuardShiftView
2. System displays current roster
3. Supervisor creates or edits a ShiftAssignment
4. System validates shift (no overlap, valid time)
5. ShiftAssignment is saved
6. NotificationService informs assigned guards

## Alternate Flows
A1. If overlap detected → show validation error  
A2. If guard unavailable → supervisor selects another guard  

## Postconditions
- ShiftAssignment stored
- Guards notified

## Business Rules
BR-HM-026 No overlapping shifts  
BR-HM-016 Notification required on change  

## Entities
Guard, ShiftAssignment

## Boundaries
GuardShiftView, ShiftEditForm

## Controls
ShiftValidator, NotificationService
