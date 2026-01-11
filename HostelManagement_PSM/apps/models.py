"""
models.py
Entity Layer — Hostel Management PSM

Derived strictly from:
- RE + Master Registry
- PIM ECB tables (WF-101 → WF-113)
- UC class tables
"""

from datetime import datetime, date
from typing import List, Optional


# =====================================================
# CORE USERS / ROLES
# =====================================================

class Student:
    def __init__(self, student_id: str, name: str, hostel_id: Optional[str]):
        self.student_id = student_id
        self.name = name
        self.hostel_id = hostel_id
        self.academic_standing = "GOOD"
        self.conduct_history = []
        self.disciplinary_status = "NONE"


class Caretaker:
    def __init__(self, staff_id: str, name: str, assigned_hostels: List[str]):
        self.staff_id = staff_id
        self.name = name
        self.assigned_hostels = assigned_hostels


class Warden:
    def __init__(self, staff_id: str, name: str, supervised_hostels: List[str]):
        self.staff_id = staff_id
        self.name = name
        self.supervised_hostels = supervised_hostels


class SuperAdmin:
    def __init__(self, admin_id: str, name: str, email: str):
        self.admin_id = admin_id
        self.name = name
        self.email = email


# =====================================================
# HOSTEL & STAFFING (WF-103, WF-106)
# =====================================================

class Hostel:
    def __init__(self, hostel_id: str, name: str, hostel_type: str, address: str, capacity: int):
        self.hostel_id = hostel_id
        self.name = name
        self.type = hostel_type
        self.address = address
        self.capacity = capacity
        self.status = "ACTIVE"
        self.created_at = datetime.now()


class StaffAssignment:
    def __init__(self, assignment_id: str, staff_id: str, hostel_id: str, role: str):
        self.assignment_id = assignment_id
        self.staff_id = staff_id
        self.hostel_id = hostel_id
        self.role = role              # WARDEN / CARETAKER
        self.assigned_at = datetime.now()
        self.revoked_at = None


# =====================================================
# ROOM MANAGEMENT (WF-103, WF-104, WF-109)
# =====================================================

class Room:
    def __init__(self, room_id: str, capacity: int):
        self.room_id = room_id
        self.capacity = capacity
        self.occupancy = 0
        self.hostel_id = None
        self.room_number = None
        self.room_type = "STANDARD"
        self.floor = None


class RoomAllocation:
    def __init__(self, allocation_id: str, student_id: str, room_id: str):
        self.allocation_id = allocation_id
        self.student_id = student_id
        self.room_id = room_id
        self.allocated_at = datetime.now()


class RoomAssignmentHistory:
    def __init__(self, student_id: str, old_room: str, new_room: str):
        self.student_id = student_id
        self.old_room = old_room
        self.new_room = new_room
        self.changed_at = datetime.now()


class RoomChangeRequest:
    def __init__(self, request_id: str, student_id: str, reason: str):
        self.request_id = request_id
        self.student_id = student_id
        self.reason = reason
        self.status = "PENDING"


class RoomVacationRequest:
    def __init__(self, request_id: str, student_id: str, vacation_date: date):
        self.request_id = request_id
        self.student_id = student_id
        self.vacation_date = vacation_date
        self.status = "PENDING"


class ClearanceRecord:
    def __init__(self, record_id: str, student_id: str, cleared_by: str):
        self.record_id = record_id
        self.student_id = student_id
        self.cleared_by = cleared_by
        self.cleared_at = datetime.now()


# =====================================================
# LEAVE & ATTENDANCE (WF-101)
# =====================================================

class LeaveRequest:
    def __init__(self, request_id: str, student_id: str, start_date: date, end_date: date):
        self.request_id = request_id
        self.student_id = student_id
        self.start_date = start_date
        self.end_date = end_date
        self.reason = None
        self.status = "PENDING"
        self.remarks = None


class SupportingDocument:
    def __init__(self, doc_id: str, request_id: str, file_name: str, file_type: str, file_link: str):
        self.doc_id = doc_id
        self.request_id = request_id
        self.file_name = file_name
        self.file_type = file_type
        self.file_link = file_link


class AttendanceRecord:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self.on_leave = False
        self.dates: List[date] = []


# =====================================================
# COMPLAINTS (WF-102)
# =====================================================

class Complaint:
    def __init__(self, complaint_id: str, student_id: str, category: str, description: str):
        self.complaint_id = complaint_id
        self.student_id = student_id
        self.category = category
        self.description = description
        self.status = "OPEN"
        self.created_at = datetime.now()


class ComplaintResolution:
    def __init__(self, complaint_id: str, resolved_by: str, remarks: str):
        self.complaint_id = complaint_id
        self.resolved_by = resolved_by
        self.remarks = remarks
        self.resolved_at = datetime.now()


# =====================================================
# FINES (WF-105)
# =====================================================

class Fine:
    def __init__(self, fine_id: str, student_id: str, amount: float, reason: str):
        self.fine_id = fine_id
        self.student_id = student_id
        self.amount = amount
        self.reason = reason
        self.status = "UNPAID"
        self.imposed_at = datetime.now()


# =====================================================
# SECURITY & VISITOR (WF-107, WF-108)
# =====================================================

class Guard:
    def __init__(self, guard_id: str, name: str, phone: str, status: str):
        self.guard_id = guard_id
        self.name = name
        self.phone = phone
        self.status = status


class ShiftAssignment:
    def __init__(self, shift_id: str, guard_id: str, start_time: datetime, end_time: datetime, location: str):
        self.shift_id = shift_id
        self.guard_id = guard_id
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.status = "ACTIVE"


class IncidentReport:
    def __init__(self, report_id: str, description: str, severity: str):
        self.report_id = report_id
        self.description = description
        self.severity = severity
        self.status = "OPEN"
        self.logged_at = datetime.now()


class Visitor:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone


class VisitRequest:
    def __init__(self, request_id: str, visit_date: date):
        self.request_id = request_id
        self.visit_date = visit_date
        self.status = "PENDING"


class VisitLog:
    def __init__(self, log_id: str, entry_time: datetime, exit_time: Optional[datetime]):
        self.log_id = log_id
        self.entry_time = entry_time
        self.exit_time = exit_time


# =====================================================
# NOTICE MANAGEMENT (WF-110)
# =====================================================

class Notice:
    def __init__(self, notice_id: str, title: str, description: str, priority: str):
        self.notice_id = notice_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "DRAFT"
        self.start_date = None
        self.end_date = None


class NoticeTarget:
    def __init__(self, target_id: str, notice_id: str, hostel_id: str, scope_type: str):
        self.target_id = target_id
        self.notice_id = notice_id
        self.hostel_id = hostel_id
        self.scope_type = scope_type


class Attachment:
    def __init__(self, attachment_id: str, notice_id: str, file_name: str, file_type: str, file_size: int):
        self.attachment_id = attachment_id
        self.notice_id = notice_id
        self.file_name = file_name
        self.file_type = file_type
        self.file_size = file_size


class NoticeReadStatus:
    def __init__(self, notice_id: str, student_id: str):
        self.notice_id = notice_id
        self.student_id = student_id
        self.read_at = datetime.now()


class ArchivedNotice:
    def __init__(self, notice_id: str):
        self.notice_id = notice_id
        self.archived_at = datetime.now()


# =====================================================
# REPORTS (WF-111)
# =====================================================

class Report:
    def __init__(self, report_id: str, report_type: str):
        self.report_id = report_id
        self.type = report_type
        self.status = "GENERATED"
        self.generated_at = datetime.now()


class ReportParameters:
    def __init__(self, date_range: str, filters: dict):
        self.date_range = date_range
        self.filters = filters


class ReportData:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data


class ArchivedReport:
    def __init__(self, report_id: str):
        self.report_id = report_id
        self.archived_at = datetime.now()


# =====================================================
# GUEST ROOM & EXTENDED STAY (WF-112, WF-113)
# =====================================================

class GuestRoom:
    def __init__(self, room_id: str, hostel_id: str):
        self.room_id = room_id
        self.hostel_id = hostel_id
        self.status = "AVAILABLE"


class GuestRoomBooking:
    def __init__(self, booking_id: str, student_id: str):
        self.booking_id = booking_id
        self.student_id = student_id
        self.status = "PENDING"
        self.check_in_date = None
        self.check_out_date = None
        self.guest_name = None
        self.guest_contact = None
        self.guest_identity_id = None
        self.booking_date = datetime.now()


# =====================================================
# GUEST ROOM ENTITIES
# =====================================================

class GuestIdentity:
    def __init__(self, identity_id: str, id_type: str, id_number: str):
        self.identity_id = identity_id
        self.id_type = id_type
        self.id_number = id_number
        self.verified = False
        self.verified_at = None


class RoomInspection:
    def __init__(self, inspection_id: str, booking_id: str, room_id: str):
        self.inspection_id = inspection_id
        self.booking_id = booking_id
        self.room_id = room_id
        self.damage_found = False
        self.damage_description = None
        self.estimated_cost = 0.0
        self.inspected_at = datetime.now()
        self.inspected_by = None


class ExtendedStayApplication:
    def __init__(self, application_id: str, student_id: str, reason: str):
        self.application_id = application_id
        self.student_id = student_id
        self.reason = reason
        self.status = "PENDING"
        self.start_date = None
        self.end_date = None
        self.approval_date = None
        self.faculty_approval = False
        self.authorization_doc_id = None
        self.charges_id = None
        self.payment_status = "UNPAID"


# =====================================================
# EXTENDED STAY ENTITIES
# =====================================================

class VacationPeriod:
    def __init__(self, period_id: str, period_name: str, start_date: date, end_date: date):
        self.period_id = period_id
        self.period_name = period_name
        self.start_date = start_date
        self.end_date = end_date
        self.period_type = "VACATION"


class StayCharge:
    def __init__(self, charge_id: str, application_id: str):
        self.charge_id = charge_id
        self.application_id = application_id
        self.base_amount = 0.0
        self.facility_charges = 0.0
        self.tax = 0.0
        self.total_amount = 0.0
        self.payment_deadline = None
        self.payment_status = "UNPAID"


class AuthorizationDocument:
    def __init__(self, doc_id: str, student_id: str, faculty_name: str):
        self.doc_id = doc_id
        self.student_id = student_id
        self.faculty_name = faculty_name
        self.faculty_email = None
        self.verification_status = False
        self.verified_at = None
        self.document_link = None


# =====================================================
# SUPPORTING ENTITIES
# ============================================================

class DisciplinaryReport:
    def __init__(self, report_id: str, student_id: str, severity: str):
        self.report_id = report_id
        self.student_id = student_id
        self.severity = severity
        self.status = "OPEN"
        self.reported_at = datetime.now()
        self.reported_by = None
        self.description = None


class Inventory:
    def __init__(self, item_id: str, item_name: str, quantity: int):
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity
        self.location = None
        self.category = None
        self.last_updated = datetime.now()


class ResourceRequest:
    def __init__(self, request_id: str, resource_type: str, quantity: int):
        self.request_id = request_id
        self.resource_type = resource_type
        self.quantity = quantity
        self.status = "PENDING"
        self.requested_by = None
        self.requested_at = datetime.now()


# =====================================================
# SYSTEM
# =====================================================

class SystemAuditLog:
    def __init__(self, log_id: str, details: str):
        self.log_id = log_id
        self.details = details
        self.timestamp = datetime.now()
