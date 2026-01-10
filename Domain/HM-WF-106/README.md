# HM-WF-106 — Hostel Setup & Staffing Workflow Realization Map

| Step | Node / UC Code                  | Actor         | Trigger / Input                       | Output / Result                        | BR  |
|------|--------------------------------|---------------|--------------------------------------|----------------------------------------|-----|
| 1    | HM-UC-004A: Create Hostel       | Super Admin   | Initiate hostel creation             | Hostel created (inactive)               | BR-HM-025 |
| 2    | HM-UC-005A: Assign Warden       | Super Admin   | Hostel created                        | Warden assigned                         | -   |
| 3    | HM-UC-005B: Assign Caretaker    | Super Admin   | Warden assigned                        | Caretaker assigned                       | -   |
| 4    | D1: All Mandatory Staff Assigned?| System       | Warden + Caretaker assigned           | Yes → Activate hostel <br> No → Remain inactive | BR-HM-019 |
| 5    | HM-UC-004B: Activate Hostel     | Super Admin   | All staff assigned (D1=Yes)          | Hostel active and operational           | BR-HM-008 |
| 6    | END-1: Hostel Active & Operational | System     | Activation successful                  | Hostel ready for use                     | BR-HM-008 |
| 7    | END-2: Hostel Created but Not Operational | System | Missing staff (D1=No)              | Hostel remains inactive                  | -   |
