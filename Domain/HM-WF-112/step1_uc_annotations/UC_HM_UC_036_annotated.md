# HM-UC-036: Request Guest Room

**Trigger:** Student navigates to **"Guest Room Booking" section** [Boundary] and clicks **"Request Guest Room"** [User Action].

**Main Flow:**
1.  Student clicks 'Request Guest Room' button.
2.  System displays **guest room booking form** [Boundary].
3.  Student enters **guest name** [Entity: GuestRoomBooking.guestName].
4.  Student enters **guest contact details (phone, email)** [Entity: GuestRoomBooking.guestPhone, GuestRoomBooking.guestEmail].
5.  Student selects **check-in date** [Entity: GuestRoomBooking.checkInDate].
6.  Student selects **check-out date** [Entity: GuestRoomBooking.checkOutDate].
7.  Student enters **purpose/reason** [Entity: GuestRoomBooking.purpose] for guest visit.
8.  Student clicks **'Check Availability'** [User Action].
9.  System displays **available guest rooms** [Entity: GuestRoom.roomNumber, GuestRoom.status] for selected dates.
10. Student selects **preferred guest room** [Entity: GuestRoomBooking.selectedRoom].
11. Student reviews booking summary (**guest details**, **dates**, **room**, **charges** [Entity: GuestRoomBooking.totalCharges]).
12. Student clicks **'Submit Booking Request'** [User Action].
13. System validates form data.
14. System records booking request with **status='Pending'** [Entity: GuestRoomBooking.bookingStatus].
15. System sends notification to **Caretaker** [Actor].
16. System displays **confirmation message** [Boundary] with **request ID** [Entity: GuestRoomBooking.requestId].
17. System sends acknowledgment notification to student.