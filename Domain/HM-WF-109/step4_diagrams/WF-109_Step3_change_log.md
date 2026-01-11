# WF-109 — Step-3 Change Log

Central Stateful Entity: RoomVacationRequest

New state model added:

States:
Draft
Pending
Approved
Rejected
Completed

New attributes added:
submittedAt
approvedAt
rejectedAt
completedAt

New operations added:
submit()
approve()
reject()
complete()

Reason:
These operations and attributes were derived from the state transitions
of the Room Vacation workflow.

All other entities and controls remain unchanged from Step-2.
