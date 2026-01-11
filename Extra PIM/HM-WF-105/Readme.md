# Hostel Management Module: Fine Management Workflow (HM-WF-105)

## Overview
[cite_start]This repository contains the **Platform Independent Model (PIM-lite)** artifacts for the **Fine Management Workflow (HM-WF-105)**[cite: 29]. [cite_start]This workflow covers the end-to-end process of a Caretaker imposing fines, students viewing them, and Wardens monitoring/escalating issues[cite: 31].

## Workflow Details
* **Workflow ID:** HM-WF-105
* [cite_start]**Trigger:** Caretaker initiates Impose and Record Fine (HM-UC-016)[cite: 31].
* [cite_start]**Key Actors:** Caretaker, Student, Warden, System[cite: 31].
* [cite_start]**End States:** Fine Recorded/Tracked (END-1) or Escalated for Disciplinary Review (END-2)[cite: 31].

## Directory Structure & Deliverables

### Step 1: Use Case Analysis & Initial EBC
* **`/step1_uc_annotations/`**: Annotated text for HM-UC-016, HM-UC-017, and HM-UC-018 identifying Boundaries, Entities, and Attributes.
* **`/step1_tables/`**: CSV extraction of classes (`Fine`, `Student`, `DisciplinaryReport`) and their stereotypes.
* **`/step1_diagrams/`**: Initial Entity-Boundary-Control (EBC) class diagrams (PlantUML) for each Use Case and the merged view.

### Step 2: Sequence-Driven Interaction
* [cite_start]**`/step2_sequences/`**: Sequence diagram for the anchor Use Case **HM-UC-016 (Impose Fine)**, detailing interactions between the Caretaker, FineImpositionForm, FineController, and NotificationService[cite: 244].
* **`/step2_diagrams/`**: Updated Domain Class Diagram adding operations discovered during sequence analysis (e.g., `create()`, `addFine()`).

### Step 3: State-Specific Behavior
* [cite_start]**`/step3_states/`**: State Machine Diagram for the **Fine** entity, covering lifecycle states: `Unpaid` → `Paid` or `Escalated`[cite: 134].
* **`/step3_diagrams/`**: Updated Domain Class Diagram adding state-driven attributes (e.g., `paidAt`) and logic (`monitorThresholds`).

### Step 4: Workflow Realization & Final Model
* **`/step4_workflow/`**:
    * **Workflow Realization Map:** Mapping of Workflow Nodes (N1-N4, D1) to Class Operations.
    * **Completeness Note:** Analysis of coverage, structure, and gaps (e.g., BR-HM-023 timeout clarification).
* **`/step4_diagrams/`**: **Final Domain EBC Class Diagram** representing the complete PIM-lite model.

## Key Business Rules Implemented
The domain model enforces the following critical business rules:
* [cite_start]**BR-HM-013 (Validation):** Fines must have a positive amount and a reason[cite: 133].
* [cite_start]**BR-HM-014 (Lifecycle):** Fines start as 'Unpaid'; thresholds trigger escalation[cite: 134].
* [cite_start]**BR-HM-022 (Evidence):** File uploads must meet size/format limits[cite: 136].
* **BR-HM-012 (Data Scoping):** Students view only their own fines; [cite_start]Wardens view their assigned hostels[cite: 135].

## Tools Used
* **PlantUML:** Used for all UML diagrams (Class, Sequence, State Machine).
* **Markdown:** Used for annotations and tables.