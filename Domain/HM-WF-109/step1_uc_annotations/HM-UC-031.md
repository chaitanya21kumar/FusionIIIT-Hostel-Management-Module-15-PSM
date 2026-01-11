# HM-UC-031 — Complete Room Vacation

## Primary Actor
Hostel Office

## Preconditions
ClearanceCertificate is issued.

## Main Flow
1. Hostel Office opens VacationFinalizationView.
2. System deallocates Room.
3. System archives StudentHostelRecord.
4. System generates VacationCompletionReport.

## Business Rules
BR-HM-042 Room must be cleared before finalization.

## Entities
Room, StudentHostelRecord, VacationCompletionReport

## Boundaries
VacationFinalizationView

## Controls
VacationFinalizationController
