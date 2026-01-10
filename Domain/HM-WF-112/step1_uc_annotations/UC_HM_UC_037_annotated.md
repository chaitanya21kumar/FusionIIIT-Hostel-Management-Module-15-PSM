# [cite_start]HM-UC-037: Approve and Manage Booking [cite: 188]

**Trigger:** Caretaker receives notification... and navigates to **"Guest Room Management" section** [Boundary].

**Main Flow (Approval):**
1.  Caretaker accesses **'Pending Guest Room Requests' dashboard** [Boundary].
2.  Caretaker selects a **booking request** [Entity: GuestRoomBooking] to review.
3.  System displays request details (**student info**, **guest details**, **dates**, **reason**).
4.  Caretaker verifies **student eligibility** [Entity: Student.eligibilityStatus].
5.  Caretaker checks **guest room availability** [Entity: GuestRoom.availability].
6.  Caretaker reviews **student's hostel conduct history** [Entity: Student.conductHistory].
7.  Caretaker makes decision:
    * (If Rejecting): enters **rejection reason** [Entity: GuestRoomBooking.rejectionReason].
8.  Caretaker clicks **'Approve Booking'** [User Action].
9.  System updates **booking status** to **'Approved'** [Entity: GuestRoomBooking.bookingStatus].
10. System reserves **guest room** [Entity: GuestRoom.reservationStatus].
11. System sends approval notification...

**Main Flow (Check-In):**
12. On check-in date, Caretaker navigates to **'Approved Bookings'** [Boundary/View].
13. Caretaker selects booking for check-in.
14. Caretaker verifies **guest identity (ID proof)** [Entity: GuestIdentity.idProofType, GuestIdentity.idProofNumber].
15. Caretaker records **guest details** and documents.
16. Caretaker assigns **room key** [Entity: RoomKey].
17. System updates **booking status** to **'Checked-In'** [Entity: GuestRoomBooking.bookingStatus].
18. System records **check-in timestamp** [Entity: GuestRoomBooking.actualCheckInTime].

**Main Flow (Check-Out):**
19. On check-out date, Caretaker selects booking for check-out.
20. Caretaker conducts **room inspection** [Boundary: InspectionChecklist].
21. Caretaker collects room key.
22. If no damages...
23. System updates **booking status** to **'Completed'** [Entity: GuestRoomBooking.bookingStatus].
24. System updates **room status** to **'Available'** [Entity: GuestRoom.status].