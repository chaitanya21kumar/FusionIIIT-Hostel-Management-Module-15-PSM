## Workflow Realization Map
### HM-WF-104 — Student Room Change Workflow

This document maps the workflow steps of HM-WF-104 to the corresponding
PIM artifacts to ensure full realization and traceability.

---

### 1. Workflow → Use Case Mapping

| Workflow Step | Use Case |
|--------------|----------|
| Submit Room Change Request | HM-UC-013 |
| Validate & Record Request | HM-UC-013 |
| Review Request | HM-UC-014 |
| Check Room Availability | HM-UC-014 |
| Check Policy Compliance | HM-UC-014 |
| Approve / Reject Request | HM-UC-014 |
| Update Room Allocation | HM-UC-015 |
| Notify Student | HM-UC-015 |
| View Request Status | HM-UC-013 |

---

### 2. Workflow → Sequence Diagram Mapping

| Workflow Step | Sequence Diagram |
|--------------|-----------------|
| End-to-End Main Flow | HM-WF-104 MainFlow Sequence |

---

### 3. Workflow → State Diagram Mapping

| Workflow Condition | RoomChangeRequest State |
|-------------------|------------------------|
| Request Submitted | Submitted |
| Under Review | UnderReview |
| Dual Approval Granted | Approved |
| Room Reassigned | AllocationUpdated |
| Process Completed | Completed |
| Request Rejected | Rejected_* |

---

### 4. Workflow → EBC Domain Mapping

| Workflow Responsibility | Domain Element |
|------------------------|----------------|
| Request Submission | RoomChangeRequestUI |
| Validation | RoomChangeValidationController |
| Availability Check | RoomAvailabilityController |
| Policy Compliance | RoomPolicyController |
| Dual Approval | RoomChangeApprovalController |
| Room Reallocation | RoomAllocationUI |
| Notification | NotificationService |

---

### Conclusion

All activities and decisions of workflow HM-WF-104 are explicitly
realized through corresponding use cases, sequence diagrams,
state transitions, and EBC domain components.
