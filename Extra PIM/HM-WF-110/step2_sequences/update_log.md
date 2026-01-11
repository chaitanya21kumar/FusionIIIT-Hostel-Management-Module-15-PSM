## Step 2 – Update Log (After Sequence Modeling)

### Context
Step 2 sequence diagrams for HM-UC-032 (Create & Publish Notice) and
HM-UC-033 (View & Store Notice) were created to validate interaction flow
and responsibility allocation across Boundary, Control, and Entity layers.

### Key Updates & Refinements

1. **Control Responsibilities Clarified**
   - Introduced clear separation between:
     - NoticeValidationController
     - NoticePublishController
     - NoticeQueryController
     - NoticeArchiveController
   - Avoided overloading a single controller with multiple concerns.

2. **Entity Lifecycle Alignment**
   - Notice entity lifecycle refined to explicitly support:
     Draft → Published → Archived → Deleted
   - Archive behavior moved under NoticeArchiveController.

3. **Read Tracking Formalized**
   - NoticeReadStatus entity explicitly modeled after sequence validation.
   - Responsibility for read marking assigned to NoticeTrackingController.

4. **Notification Decoupling**
   - NotificationService modeled as independent Control component.
   - Publishing logic does not embed notification logic directly.

5. **Boundary Simplification**
   - UI components limited strictly to data collection and display.
   - No business logic retained in Boundary classes.

6. **Consistency Check**
   - All sequence participants now trace back to:
     - Step 1 Tables
     - Step 1 Class Diagrams
   - No new entities introduced without UC justification.

### Outcome
The domain model is now interaction-validated, cohesive, and ready for:
- State Machine modeling (Step 3)
- Workflow/activity modeling (Step 4)
![alt text](image.png)