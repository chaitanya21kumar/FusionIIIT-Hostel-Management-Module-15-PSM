WF-109 Workflow Realisation Map

Submit Request -> RoomVacationWorkflowController.submitRequest()
Generate Checklist -> VacationRequestController.generateChecklist()
Verify Clearance -> ClearanceController.verifyClearance()
Issue Certificate -> ClearanceController.issueCertificate()
Approve Vacation -> RoomVacationRequest.approve()
Finalize Vacation -> VacationFinalizationController.finalizeVacation()
Deallocate Room -> Room.deallocate()
Archive Student Data -> StudentHostelRecord.archiveHistory()
Generate Report -> VacationCompletionReport.generate()

Each workflow step is mapped to a class operation in the final domain model.
