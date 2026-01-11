## UC: HM-UC-013 — Submit Room Change Request

### Annotated Flow (EBC)

M1. Student opens room change request form  
(Boundary: RoomChangeRequestUI)

M2. System displays current room details  
(Boundary)

M3. Student enters reason for room change  
(Boundary) → RoomChangeRequest.reason  
(Entity)

M4. Student optionally selects preferred room/hostel  
(Boundary) → RoomPreference  
(Entity)

M5. Student submits request  
(Boundary)

M6. System validates request data  
(Control: RoomChangeValidationController)  
[BR-HM-115]

M7. System records request with status = Pending  
(Control) → RoomChangeRequest  
(Entity)

M8. System assigns request ID and notifies Caretaker & Warden  
(Control: NotificationService)

Result: Room change request successfully submitted
