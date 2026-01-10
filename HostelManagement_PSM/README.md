# Hostel Management Module — Platform Specific Model (PSM)

## 1. Purpose
This directory contains the **Platform Specific Model (PSM)** for the Hostel Management (HM) module of the Fusion ERP system.

The PSM is derived **strictly** from:
- Final Requirements Engineering (RE) artifacts
- Platform Independent Model (PIM)
- Entity–Boundary–Control (EBC) class tables
- Use Case (UC) specifications
- Workflow (WF) definitions
- Business Rules (BR-HM-xxx)
- Traceability matrices

No assumptions beyond the provided documents have been introduced.

---

## 2. Source Artifacts

### Requirements Engineering (RE)
- Business Rules: `HM_New_BRs_1to18_Complete2.docx`
- Use Cases: `HM_New_UCs_complete2.docx`
- Workflows: `HM_New_WFs_complete.docx`
- Traceability Matrix: `Traceability matrix.docx`
- Master Registry: `Master_registry_final.xlsx`

### Platform Independent Model (PIM)
- ECB tables for workflows:
  - HM-WF-101 → HM-WF-113
- Class tables per Use Case
- Sequence and interaction models

---

## 3. Architectural Mapping (ECB)

| Layer | PSM File | Source |
|-----|---------|-------|
| Entity | models.py | PIM Entity classes |
| Control | services.py | PIM Control classes |
| Policy | policy.py | Business Rules (BR-HM-xxx) |
| Boundary | views.py | PIM Boundary classes |
| Workflow Events | events.py | WF specifications |
| DTO | serializers.py | UC I/O contracts |

---

## 4. Workflow Coverage

All workflows defined in RE are covered:

- HM-WF-101 — Student Leave Request
- HM-WF-102 — Complaint Resolution
- HM-WF-103 — New Student Room Allotment
- HM-WF-104 — Room Change
- HM-WF-105 — Fine Management
- HM-WF-106 — Hostel Setup & Staffing
- HM-WF-107 — Security & Guard Shift Management
- HM-WF-108 — Visitor / Entry Management
- HM-WF-109 — Room Vacation & Clearance
- HM-WF-110 — Notice Management
- HM-WF-111 — Staff Report Generation
- HM-WF-112 — Guest Room Booking
- HM-WF-113 — Extended Stay During Vacations

---

## 5. Traceability Guarantee
Every:
- Use Case (HM-UC-xxx)
- Workflow (HM-WF-xxx)
- Business Rule (BR-HM-xxx)

is mapped to:
- Service function
- Policy rule
- Entity state

via **RTM_Map.xlsx**.

---

## 6. Notes
- This PSM is **framework-agnostic** (no Django/JPA assumptions).
- Persistence, API transport, and UI rendering are intentionally abstracted.
- Focus is correctness, traceability, and architectural fidelity.
