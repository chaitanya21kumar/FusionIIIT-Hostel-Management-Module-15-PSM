# HM-UC-040: Manage Extended Stay Operations

**Trigger:** Extended stay application is approved, or vacation period begins.

**Main Flow:**
1. Upon application approval, system automatically triggered.
2. System retrieves student's current room allocation.
3. System reserves the **room** for vacation period [Entity: RoomReservation].
4. System updates **room occupancy** calendar.
5. System marks room as **'Reserved - Extended Stay'** [Entity: Room.status].
6. System blocks room from maintenance scheduling.
7. System retrieves extended stay duration.
8. System fetches configured per-day vacation rate.
9. System calculates **base charges** and **facility charges** [Entity: StayCharge.baseAmount, StayCharge.facilityCharges].
10. System generates **total charge amount** [Entity: StayCharge.totalAmount].
11. System creates **charge record** linked to student account [Entity: StayCharge].
12. System sends charge notification to student.
13. System monitors **payment status** [Entity: StayCharge.paymentStatus].
14. Student submits payment proof... Caretaker verifies... System updates status to **'Paid'**.
15. Caretaker coordinates **mess services** [Entity: ServicePlan.messSchedule].
16. Caretaker schedules **cleaning staff** [Entity: ServicePlan.cleaningSchedule].
17. Caretaker ensures **security guard coverage** [Entity: ServicePlan.securityCoverage].
18. During vacation, Caretaker monitors **student presence** [Entity: VacationAttendance.status].
19. If **rule violation** reported [Entity: Violation.type, Violation.severity].
20. Caretaker documents violation.
21. System links violation to extended stay record.
22. Caretaker imposes fine... may **terminate stay** [Entity: ExtendedStayApplication.status].