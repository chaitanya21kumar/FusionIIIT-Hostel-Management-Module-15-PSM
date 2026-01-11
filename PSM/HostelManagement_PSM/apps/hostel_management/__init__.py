"""
Hostel Management PSM Module

This module provides the Platform Specific Model (PSM) for the
Hostel Management system, implementing all 13 workflows (WF-101 to WF-113).

Architecture:
- Entity Layer: models.py
- Control Layer: services.py
- Policy Layer: policy.py (Business Rules)
- Boundary Layer: views.py
- Events Layer: events.py
- Serializers: serializers.py
- URL Mappings: urls.py
"""

# PHASE 3: Export commonly used entities for easier imports
from .models import (
    # Core Users
    Student, Caretaker, Warden, SuperAdmin,
    
    # Hostel & Rooms
    Hostel, Room, RoomAllocation, RoomChangeRequest,
    
    # Leave Management
    LeaveRequest, AttendanceRecord,
    
    # Complaints & Fines
    Complaint, Fine,
    
    # Security
    Guard, ShiftAssignment, IncidentReport,
    
    # Visitors
    Visitor, VisitRequest, VisitLog,
    
    # Room Vacation
    RoomVacationRequest, ClearanceRecord,
    
    # Notices & Reports
    Notice, Report,
    
    # Guest Rooms & Extended Stay
    GuestRoomBooking, ExtendedStayApplication,
)

__all__ = [
    'Student', 'Caretaker', 'Warden', 'SuperAdmin',
    'Hostel', 'Room', 'RoomAllocation', 'RoomChangeRequest',
    'LeaveRequest', 'AttendanceRecord',
    'Complaint', 'Fine',
    'Guard', 'ShiftAssignment', 'IncidentReport',
    'Visitor', 'VisitRequest', 'VisitLog',
    'RoomVacationRequest', 'ClearanceRecord',
    'Notice', 'Report',
    'GuestRoomBooking', 'ExtendedStayApplication',
]