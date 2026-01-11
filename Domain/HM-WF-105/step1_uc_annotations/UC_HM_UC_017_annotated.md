# Use Case: HM-UC-017 View and Track Fines

**Text:**
The **Student** (Actor) navigates to the **StudentFineDashboard** (Boundary). The System retrieves a list of **Fines** (Entity) associated with the Student account.

The Student views details including **ReferenceID** (Attribute), **ViolationCategory** (Attribute), **Amount** (Attribute), **PaymentStatus** (Attribute), and **PaymentDate** (Attribute).

The Student can filter by status (Unpaid/Paid). The Student selects a specific Fine to view **Evidence** (Attribute). The Student clicks **DownloadReport** (Action). The System generates a **FineHistoryReport** (Entity/Document).

**Annotations:**
* **Student**: Actor
* **StudentFineDashboard**: Boundary
* **Fine**: Entity
* **ReferenceID**: Attribute (Fine)
* **ViolationCategory**: Attribute (Fine)
* **Amount**: Attribute (Fine)
* **PaymentStatus**: Attribute (Fine)
* **PaymentDate**: Attribute (Fine)
* **Evidence**: Attribute (Fine)
* **FineHistoryReport**: Entity (Output)