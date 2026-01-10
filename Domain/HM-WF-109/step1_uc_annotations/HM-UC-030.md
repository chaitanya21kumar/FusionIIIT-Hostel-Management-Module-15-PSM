# HM-UC-030 — Verify Clearance Requirements

## Primary Actor
Hostel Staff

## Preconditions
RoomVacationRequest exists.

## Main Flow
1. Staff opens ClearanceVerificationView.
2. System displays ClearanceChecklist.
3. Staff records RoomInspection.
4. System verifies clearance.
5. System issues ClearanceCertificate.

## Business Rules
BR-HM-041 All clearances must be verified before approval.

## Entities
ClearanceChecklist, RoomInspection, ClearanceCertificate

## Boundaries
ClearanceVerificationView

## Controls
ClearanceController
