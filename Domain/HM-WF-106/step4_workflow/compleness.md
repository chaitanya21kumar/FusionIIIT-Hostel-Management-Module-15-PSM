# HM-WF-106 — Step 4 Workflow: Hostel Activation

## Node N4: Manage Hostel Status (Activate)
- **Use Case:** HM-UC-004B
- **Actor:** Super Admin
- **Description:** Set the hostel status to Active after verifying all mandatory staff are assigned.
- **Precondition:** 
  - All required staff (Warden and Caretaker) assigned (D1 = Yes)
  - Hostel exists in the system (N1 completed)
- **Trigger:** Super Admin chooses to activate the hostel
- **Postcondition:** 
  - Hostel becomes operational
  - Rooms and students can be allocated
- **Business Rule Validation:** BR-HM-008

## End State
- **END-1:** Hostel Active and Operational
