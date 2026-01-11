## Workflow Realization Map
### HM-WF-108 – Staff Notice Management

This document maps workflow steps to their realizing PIM artifacts,
ensuring traceability and alignment.

---

### 1. Workflow → Use Case Mapping

| Workflow Step | Use Case |
|--------------|----------|
| Create Notice | HM-UC-032 |
| Validate Notice | HM-UC-032 |
| Publish Notice | HM-UC-032 |
| Notify Students | HM-UC-032 |
| View Notice | HM-UC-033 |
| Track Read Status | HM-UC-033 |
| Archive Notice | HM-UC-033 (System) |
| Delete Notice | HM-UC-032 |

---

### 2. Workflow → Sequence Diagram Mapping

| Workflow Step | Sequence Diagram |
|--------------|-----------------|
| Notice Creation & Validation | HM-UC-032 Sequence |
| Notification Dispatch | HM-UC-032 Sequence |
| Student Viewing | HM-UC-033 Sequence |
| Read Tracking | HM-UC-033 Sequence |
| Expiry & Archival | HM-UC-033 Sequence (System Action) |

---

### 3. Workflow → State Diagram Mapping

| Workflow Condition | Notice State |
|-------------------|-------------|
| Draft Notice | Draft |
| Notice Published | Published |
| Notice Expired | Archived |
| Notice Deleted | Deleted |

---

### 4. Workflow → EBC Domain Mapping

| Workflow Responsibility | Domain Element |
|------------------------|----------------|
| Data Entry | NoticeFormUI |
| Validation | NoticeValidationController |
| Publishing | NoticePublishController |
| Notification | NotificationService |
| Viewing | NoticeBoardUI |
| Read Tracking | NoticeTrackingController |
| Archival | NoticeArchiveController |

---

### 5. Workflow → Business Rule Mapping

| Workflow Guard | Business Rule |
|---------------|--------------|
| Content Validation | BR-HM-029 |
| Priority Handling | BR-HM-033 |
| Display Filtering | BR-HM-035 |
| Expiry Check | BR-HM-036 |
| Access Control | BR-HM-039 |

---

### Conclusion

The Staff Notice Management workflow is **fully realized** through:
- Explicit use cases
- Verified interaction flows
- Lifecycle-aware state modeling
- Cohesive EBC domain structure

This establishes a **complete and traceable PIM realization** for HM-WF-108.
