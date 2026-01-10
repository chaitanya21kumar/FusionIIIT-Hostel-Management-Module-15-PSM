# WF-108 — Step-2 Update Log
Use Cases: HM-UC-026, HM-UC-027, HM-UC-028

## New operations from sequences
VisitorController: validateVisitor(), createVisitRequest()
VisitRequest: setStatus(), updateStatus()
ApprovalController: processDecision()
ExitController: closeVisit()
VisitLog: createLog()

## New associations
VisitorController -> VisitRequest
ApprovalController -> VisitRequest
ExitController -> VisitRequest
ExitController -> VisitLog
