# Hostel Management (HM) Domain Model - PIM-lite

**Module:**Hostel Management (HM)
**Version:** v1.1

---

## Workflow Scope
**Workflow ID:** HM-WF-112
**Workflow Name:** Student Guest Room Booking
**Description:** This domain model covers the end-to-end process of a student requesting a guest room, the Caretaker's approval and management of the booking (check-in/check-out), and the handling of associated rules such as identity verification and damage inspections.

**Included Use Cases:**
* [cite_start]**HM-UC-036:** Request Guest Room [cite: 185]
* [cite_start]**HM-UC-037:** Approve and Manage Booking [cite: 187]

**Key Business Rules:**
* [cite_start]**Eligibility & Availability:** BR-HM-051, BR-HM-052, BR-HM-054, BR-HM-055 [cite: 66, 68, 72, 74]
* [cite_start]**Identity & Security:** BR-HM-053, BR-HM-056 [cite: 70, 76]
* [cite_start]**Operations (Check-out/Fines):** BR-HM-057, BR-HM-058, BR-HM-059 [cite: 78, 80, 82]

---

## Folder Structure

* **step1_uc_annotations/**
    * Contains the Use Case text annotated to identify Boundary and Entity candidates.
* **step1_tables/**
    * `classes_from_uc.csv`: Tabular extraction of potential classes from the annotated text.
* **step1_diagrams/**
    * Initial Entity-Boundary-Control (EBC) class diagrams derived strictly from Use Case text.
* **step2_sequences/**
    * Sequence diagram for the anchor Use Case (HM-UC-036) showing object interactions.
* **step2_diagrams/**
    * Updated Domain Model incorporating operations and controllers discovered during sequence modeling.
* **step3_states/**
    * State Machine diagram for the `GuestRoomBooking` entity, defining lifecycle states (Pending, Approved, CheckedIn, etc.).
* **step3_diagrams/**
    * Updated Domain Model incorporating status enums and state-driven operations (e.g., `checkIn()`, `cancel()`).
* **step4_workflow/**
    * `workflow_realization_map.md`: Mapping of workflow nodes to specific class operations.
    * `completeness.md`: Assessment of model coverage against requirements.
* **step4_diagrams/**
    * `Domain_EBC_Final.drawio`: The final, comprehensive PIM-lite domain class diagram.

---

## Tools Used
* **Modeling:** Draw.io
* **Documentation:** Markdown