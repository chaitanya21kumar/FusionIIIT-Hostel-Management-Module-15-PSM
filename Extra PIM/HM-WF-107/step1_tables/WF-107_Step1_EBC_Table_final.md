# WF-107 — STEP-1 EBC CLASS TABLE
*(Use-Case → Initial Domain Model)*  
**Workflow:** HM-WF-107 – Security & Guard Shift Management  
**Included Use Cases:** HM-UC-024, HM-UC-025

---

## Legend
- **<<Entity>>** = Business objects with persistent state  
- **<<Boundary>>** = Screens, forms, dashboards, exports  
- **<<Control>>** = Coordinators, validators, processors  

---

## STEP-1: Extracted EBC Classes

| Class Name | Stereotype | Attributes (Only from UC text) | Methods | UC IDs |
|-----------|------------|-------------------------------|--------|--------|
| **Guard** | <<Entity>> | guardID, name, phone, status | createGuard(), updateStatus() | HM-UC-024 |
| **ShiftAssignment** | <<Entity>> | shiftID, startTime, endTime, location, status | create(), update(), cancel() | HM-UC-024 |
| **IncidentReport** | <<Entity>> | reportID, timestamp, description, severity, status | log(), updateStatus() | HM-UC-025 |
| **GuardCheckIn** | <<Entity>> | checkinID, guardID, time, location | registerCheckIn() | HM-UC-025 |
| **GuardShiftView** | <<Boundary>> | — | viewRoster(), selectGuard(), createShift(), editShift() | HM-UC-024 |
| **ShiftEditForm** | <<Boundary>> | — | setTime(), setLocation(), assignGuard(), submit() | HM-UC-024 |
| **DashboardView** | <<Boundary>> | — | viewStatus(), filterData(), viewCharts() | HM-UC-025 |
| **ReportGenerator** | <<Boundary>> | — | exportPDF(), exportCSV() | HM-UC-025 |
| **ShiftValidator** | <<Control>> | — | checkOverlap(), validateShift() | HM-UC-024 |
| **NotificationService** | <<Control>> | — | notifyGuard(), sendUrgentAlert() | HM-UC-024 |
| **Aggregator** | <<Control>> | — | aggregateData() | HM-UC-025 |
| **ReportService** | <<Control>> | — | generateReport() | HM-UC-025 |

---

## STEP-1: Initial Class Relationships

*(Derived from UC narratives and EBC diagrams — no workflow logic yet)*

| From Class | Relationship | To Class | Reason |
|-----------|--------------|----------|--------|
| Guard | 1 — * | ShiftAssignment | A guard can have many shifts |
| ShiftAssignment | triggers | NotificationService | Guards are notified when shifts change |
| GuardShiftView | uses | ShiftValidator | Input validation when creating/editing shifts |
| ShiftEditForm | uses | ShiftValidator | Checks overlap & correctness |
| IncidentReport | 1 — * | GuardCheckIn | Check-ins relate to incidents |
| DashboardView | uses | Aggregator | Dashboard pulls combined security data |
| Aggregator | reads | IncidentReport | Used to build security status |
| Aggregator | reads | GuardCheckIn | Used to compute presence |
| ReportGenerator | uses | ReportService | Generates export files |

---

## STEP-1 Scope Confirmation

This table includes **ONLY** what is present in:
- HM-UC-024
- HM-UC-025  

No workflow routing, approval chains, or state logic added yet — that comes in Steps 2–4.

---

## Next steps (recommended)
Proceed to **STEP-2 — Sequence Diagrams → Class Updates (Blue)** to:
- create main-flow sequence diagrams for HM-UC-024 and HM-UC-025,
- tag messages with BR IDs,
- update the class table to add operations/associations discovered from sequences.

