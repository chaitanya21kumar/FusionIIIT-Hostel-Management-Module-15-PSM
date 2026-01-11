## Step 1 — PIM Class Table 

| Class | Stereotype | Attributes | Methods | UC IDs |
|------|------------|-----------|---------|--------|
| Student | Entity | studentID, name, currentRoomID | submitRequest(), viewStatus() | UC-013 |
| Caretaker | Entity | staffID, assignedHostels | reviewRequest(), reassignRoom() | UC-014, UC-015 |
| Warden | Entity | staffID, supervisedHostels | approveRequest(), rejectRequest() | UC-014 |
| RoomChangeRequest | Entity | requestID, reason, status | create(), approve(), reject() | UC-013, UC-014 |
| Room | Entity | roomID, capacity, occupancy | checkAvailability(), updateOccupancy() | UC-014, UC-015 |
| RoomAllocation | Entity | studentID, roomID | updateAllocation() | UC-015 |
| RoomAssignmentHistory | Entity | studentID, oldRoom, newRoom, date | recordChange() | UC-015 |
| RoomChangeRequestUI | Boundary | — | collectReason(), submitRequest() | UC-013 |
| RoomChangeReviewUI | Boundary | — | displayRequests(), captureDecision() | UC-014 |
| RoomAllocationUI | Boundary | — | reassignRoom() | UC-015 |
| RoomChangeValidationController | Control | — | validateRequest() | UC-013 |
| RoomAvailabilityController | Control | — | checkAvailability() | UC-014, UC-015 |
| RoomPolicyController | Control | — | checkCompliance() | UC-014 |
| RoomChangeApprovalController | Control | — | verifyDualApproval() | UC-014 |
| NotificationService | Control | — | notifyStudent(), notifyStaff() | UC-013, UC-015 |
