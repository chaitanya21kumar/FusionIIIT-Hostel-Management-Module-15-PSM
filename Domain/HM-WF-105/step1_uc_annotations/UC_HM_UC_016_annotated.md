# Use Case: HM-UC-016 Impose and Record Fine

**Text:**
The **Caretaker** (Actor) searches for and selects a **Student** (Entity). The Caretaker selects the **Impose Fine** option (Action) on the **StudentManagementInterface** (Boundary). The System displays the **FineImpositionForm** (Boundary).

The Caretaker selects the **ViolationCategory** (Attribute: Hostel Rule Violation, Property Damage, etc.) and enters the **FineAmount** (Attribute). The Caretaker provides a **Reason** (Attribute). The System auto-populates the **Date** (Attribute). The Caretaker optionally uploads **SupportingEvidence** (Entity/Attribute).

The Caretaker clicks **Submit** (Action). The System performs **validateFineData()** (Control) to ensure amount is positive and reason is present (checks **FinePolicies** - Control/Rule). The System validates the file format (**validateFileUpload()**).

The System creates a new **Fine** (Entity) with status "Unpaid" (Attribute). The System links the Fine to the **Student** (Association). The System triggers the **NotificationService** (Boundary) to alert the Student.

**Annotations:**
* **Caretaker**: Actor
* **Student**: Entity
* **StudentManagementInterface**: Boundary
* **FineImpositionForm**: Boundary
* **ViolationCategory**: Attribute (Fine)
* **FineAmount**: Attribute (Fine)
* **Reason**: Attribute (Fine)
* **Date**: Attribute (Fine)
* **SupportingEvidence**: Attribute (Fine - stored as reference/link)
* **Fine**: Entity
* **validateFineData**: Control Method
* **validateFileUpload**: Control Method
* **NotificationService**: Boundary