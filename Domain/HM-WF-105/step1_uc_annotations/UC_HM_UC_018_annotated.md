# Use Case: HM-UC-018 Monitor and Analyze Fines

**Text:**
The **Warden** (Actor) accesses the **FineManagementDashboard** (Boundary). The System displays a **FineSummary** (Entity/View). The Warden selects parameters for a **DisciplinaryReport** (Entity).

The Warden generates the report. The System aggregates data regarding **TotalFines** (Attribute), **RepeatOffenders** (Derived Attribute), and **ViolationTrends** (Derived Attribute). The Warden reviews the data for **Escalation** (Action/Control logic).

**Annotations:**
* **Warden**: Actor
* **FineManagementDashboard**: Boundary
* **FineSummary**: Entity (View/Aggregate)
* **DisciplinaryReport**: Entity
* **TotalFines**: Attribute (Report)
* **RepeatOffenders**: Attribute (Report)
* **ViolationTrends**: Attribute (Report)