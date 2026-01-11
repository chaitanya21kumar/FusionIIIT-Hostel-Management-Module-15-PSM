# Hostel Management Workflow — Requirements Modeling

## Module
**Hostel Management Module** — Student Room Change
---

## Version
**v1.0** — Complete PIM Workflow Modeling Deliverable
---

## Workflow ID
**HM-WF-104** — Student Room Change Workflow  
(Covers Use Cases: HM-UC-013, HM-UC-014, HM-UC-015)

---

## Objective
To model the complete lifecycle of a student room change request, from
submission through review, approval, and room reallocation, ensuring
compliance with hostel policies, room availability constraints, and
proper auditability using a **Platform Independent Model (PIM)**.

---

## Actors
- Student  
- Caretaker  
- Warden  
- System  

---

## Tools Used
- **Modeling:** Mermaid  
  (EBC class diagrams, sequence diagrams, state machine diagrams)
- **Documentation:** Markdown (`.md`) and Text (`.txt`)  
  (UC annotations, tables, workflow realization, completeness, change logs)
- **Submission:** Canvas / Academic Portal

---

## Deliverables Summary

### **Step 1 — Requirements & Structural Modeling**
- Use Case Annotations (HM-UC-013, HM-UC-014, HM-UC-015)
- PIM Class Tables (Entity–Boundary–Control)
- Individual EBC Class Diagrams per Use Case
- Merged Step-1 EBC Domain Diagram for HM-WF-104

### **Step 2 — Interaction Modeling**
- Single end-to-end **Main Flow Sequence Diagram**
- Updated EBC Domain Diagram (post interaction validation)
- Step 2 Change Log (TXT)

### **Step 3 — Behavioral Modeling**
- State Machine Diagram for `RoomChangeRequest`
- Lifecycle-aligned EBC Domain Diagram
- Step 3 Change Log (TXT)

### **Step 4 — Workflow Realization**
- Workflow Realization Map
- Workflow Completeness Verification
- Final Change Log
- Final Stable EBC Domain Diagram (PIM)

---

## Modeling Scope
- **Core Domain Entities:** RoomChangeRequest, Room, RoomAllocation,
  RoomAssignmentHistory
- **Key Controls:** Validation, Availability Check, Policy Compliance,
  Dual Approval, Notification
- **Approach:** Strict adherence to **Entity–Boundary–Control (EBC)**
- **Constraints:** No technology or implementation assumptions

---

## Workflow End States
- **Room Change Completed Successfully**
- **Room Change Rejected — No Availability**
- **Room Change Rejected — Policy Violation**
- **Room Change Rejected — Approval Missing**

All end states are explicitly modeled and traceable.

---

## Outcome
This repository contains a **complete, consistent, and traceable PIM**
for the **Student Room Change Workflow**, suitable for:

- Academic evaluation
- Design walkthroughs / viva
- Future transformation into PSM or implementation models

---
