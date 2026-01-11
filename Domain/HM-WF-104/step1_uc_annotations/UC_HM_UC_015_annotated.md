## UC: HM-UC-015 — Update Room Allocation and Notify

### Annotated Flow (EBC)

M1. System detects approved room change request  
(Control)

M2. Caretaker performs room re-allotment  
(Boundary: RoomAllocationUI)

M3. System validates new room availability  
(Control: RoomAvailabilityController)

M4. System updates student room allocation  
(Entity: RoomAllocation)

M5. System updates room occupancy counts  
(Entity: Room)

M6. System records room assignment history  
(Entity: RoomAssignmentHistory)

M7. System notifies student and caretaker  
(Control: NotificationService)

Result: Room change applied and communicated
