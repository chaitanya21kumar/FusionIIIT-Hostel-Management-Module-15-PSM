# HM-WF-106 — Hostel Setup & Staffing Workflow

## Workflow Steps (Step 2 Sequence)

### Node N2: Assign Warden to Hostel
- **Type:** Use Case
- **Actor:** Super Admin
- **Description:** Assign a Warden to the newly created hostel.
- **Precondition:** Hostel must be created successfully (N1 completed).

### Node N3: Assign Caretaker to Hostel
- **Type:** Use Case
- **Actor:** Super Admin
- **Description:** Assign a Caretaker to the hostel.
- **Precondition:** Warden must be assigned (N2 completed).

### Node D1: All Mandatory Staff Assigned?
- **Type:** Decision
- **Actor:** System
- **Description:** System checks if both Warden and Caretaker are assigned.
- **Outcomes:**
  - **Yes:** Proceed to activate hostel (N4)
  - **No:** Hostel remains inactive (END-2)

### Node N4: Manage Hostel Status (Activate)
- **Type:** Use Case
- **Actor:** Super Admin
- **Description:** Activate the hostel to make it operational.
- **Precondition:** All required staff assigned (D1=Yes).

### End States
- **END-1:** Hostel Active and Operational  
- **END-2:** Hostel Created but Not Operational

## Directed Edges (Step 2)
1. **E2:** N2 → N3 [Warden Assigned]
2. **E3:** N3 → D1 [Caretaker Assigned]
3. **E4:** D1 → N4 [Yes – All Required Staff Assigned]
4. **E5:** D1 → END-2 [No – Missing Required Staff]
5. **E6:** N4 → END-1 [Activation Successful]
