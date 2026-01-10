## UC: HM-UC-014 — Review and Process Room Change Request

### Annotated Flow (EBC)

M1. Caretaker views pending room change requests  
(Boundary: RoomChangeReviewUI)

M2. Caretaker checks room availability  
(Control: RoomAvailabilityController)  
(Entity: Room)

M3. Warden reviews policy compliance  
(Control: RoomPolicyController)  
[Hostel Policies]

M4. Caretaker & Warden enter decision remarks  
(Boundary)

M5. System validates approvals  
(Control: RoomChangeApprovalController)

M6. System updates request status  
(Entity: RoomChangeRequest)

Result: Request Approved or Rejected
