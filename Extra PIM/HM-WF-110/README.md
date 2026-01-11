# Hostel Management Workflow — Requirements Modeling

## Module
**Hostel Management Module** — Staff Notice Management

---

## Version
**v1.0** — Complete PIM Workflow Modeling Deliverable

---

## Workflow ID
**HM-WF-110** — Staff Notice Management Workflow  
(Covers Use Cases: HM-UC-032, HM-UC-033)

---

## Objective
To model the complete lifecycle of hostel notices—from creation and publication by
Caretaker/Warden to student viewing and automatic archival—using a structured,
Platform Independent Model (PIM) approach.

---

## Tools Used
- **Modeling:** Mermaid  
  (EBC class diagrams, sequence diagrams, state machine, activity workflow)
- **Documentation:** Markdown (`.md`)  
  (UC annotations, tables, workflow realization, completeness, change logs)
- **Submission:** Canvas / Academic Portal

---

## Deliverables Summary

### **Step 1 — Requirements & Structural Modeling**
- Use Case Annotations (Boundary–Control–Entity)
- PIM Class Tables
- Initial EBC Class Diagrams (per use case)

### **Step 2 — Interaction Modeling**
- Sequence Diagram: HM-UC-032 (Create & Publish Notice)
- Sequence Diagram: HM-UC-033 (View & Store Notice)
- Updated consolidated EBC Domain Model
- Step-wise Update Log

### **Step 3 — Behavioral Modeling**
- State Machine Diagram for `Notice` lifecycle  
  (Draft → Published → Archived → Deleted)
- Lifecycle-aligned EBC Class Diagram

### **Step 4 — Workflow Realization**
- Workflow Completeness Verification
- Workflow Realization Map
- Final Change Log
- Final Stable EBC Domain Model

---

## Modeling Scope
- Actors: Caretaker, Warden, Student, System
- Core Domain: Notice, Target Audience, Attachments, Read Tracking, Archival
- Focus: Clear separation of **Boundary**, **Control**, and **Entity** responsibilities
- No technology or implementation assumptions (pure PIM)

---

## Outcome
This repository contains a **complete, consistent, and traceable PIM**
for the **Staff Notice Management workflow**, suitable for:
- Academic evaluation
- Viva / design explanation
- Future transformation into PSM or implementation models

---

## Status
✔ Workflow fully realized  
✔ All use cases covered  
✔ All business rules enforced  
✔ PIM declared **final and stable**
