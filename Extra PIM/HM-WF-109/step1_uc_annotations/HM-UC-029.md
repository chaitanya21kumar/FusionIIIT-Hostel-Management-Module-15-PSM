# HM-UC-029 — Request Room Vacation

## Primary Actor
Student

## Preconditions
Student is currently allotted a room.

## Main Flow
1. Student opens RoomVacationForm.
2. Student enters intended vacation date and reason.
3. System generates ClearanceChecklist.
4. Student submits the request.
5. System creates RoomVacationRequest with status Pending.

## Business Rules
BR-HM-040 Clearance checklist must be generated before submission.

## Entities
Student, RoomVacationRequest, ClearanceChecklist

## Boundaries
RoomVacationForm

## Controls
VacationRequestController
