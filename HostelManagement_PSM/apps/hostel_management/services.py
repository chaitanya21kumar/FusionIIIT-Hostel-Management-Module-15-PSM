"""
services.py
Control Layer — Hostel Management PSM

Implements HM-UC-xxx using:
- policy.py (BR enforcement)
- models.py (entity state)
"""

from datetime import date, datetime
from typing import List, Optional

from . import policy
from .models import (
    Student, Hostel, StaffAssignment,
    Room, RoomAllocation, RoomChangeRequest, RoomAssignmentHistory,
    LeaveRequest, AttendanceRecord,
    Complaint, ComplaintResolution,
    Fine,
    Guard, ShiftAssignment, IncidentReport,
    Visitor, VisitRequest, VisitLog,
    RoomVacationRequest, ClearanceRecord,
    Notice, NoticeTarget, Attachment,
    Report, ReportParameters, ArchivedReport,
    GuestRoomBooking, ExtendedStayApplication,
    SystemAuditLog
)


# =====================================================
# WF-101 — LEAVE MANAGEMENT
# =====================================================

def apply_leave(student_id: str, hostel_status: str,
                start_date: date, end_date: date,
                reason: str, docs_attached: bool) -> LeaveRequest:
    if not policy.br_hm_101_student_must_be_active(hostel_status):
        raise ValueError("Inactive student")

    if not policy.br_hm_102_leave_dates_valid(start_date, end_date):
        raise ValueError("Invalid date range")

    if not policy.br_hm_103_leave_requires_reason_and_docs(reason, docs_attached):
        raise ValueError("Reason/docs required")

    return LeaveRequest(
        request_id=f"LR-{student_id}-{start_date}",
        student_id=student_id,
        start_date=start_date,
        end_date=end_date
    )


def process_leave(leave: LeaveRequest, role: str,
                  caretaker_hostels: List[str], student_hostel: str,
                  approve: bool, remarks: Optional[str]) -> LeaveRequest:
    if not policy.br_hm_104_only_assigned_caretaker_can_approve(
        role, caretaker_hostels, student_hostel
    ):
        raise PermissionError("Unauthorized")

    leave.status = "APPROVED" if approve else "REJECTED"
    leave.remarks = remarks
    return leave


# =====================================================
# WF-102 — COMPLAINT MANAGEMENT
# =====================================================

def submit_complaint(student_id: str, hostel_status: str,
                     category: str, description: str) -> Complaint:
    if not policy.br_hm_106_active_students_only(hostel_status):
        raise ValueError("Inactive student")

    return Complaint(
        complaint_id=f"CMP-{student_id}-{datetime.now().timestamp()}",
        student_id=student_id,
        category=category,
        description=description
    )


def resolve_complaint(complaint: Complaint, role: str, remarks: str) -> ComplaintResolution:
    if policy.br_hm_107_security_routes_to_warden(complaint.category):
        if not policy.br_hm_110_only_warden_resolves_security(role):
            raise PermissionError("Only warden")

    if not policy.br_hm_108_resolution_requires_remarks("RESOLVED", remarks):
        raise ValueError("Remarks required")

    complaint.status = "RESOLVED"
    return ComplaintResolution(
        complaint_id=complaint.complaint_id,
        resolved_by=role,
        remarks=remarks
    )


# =====================================================
# WF-103 — ROOM ALLOTMENT
# =====================================================

def allot_room(role: str, window_status: str,
               room: Room, student_id: str) -> RoomAllocation:
    if not policy.br_hm_111_allotment_window_open(window_status):
        raise ValueError("Window closed")

    if not policy.br_hm_113_only_superadmin_bulk_allot(role):
        raise PermissionError("Only superadmin")

    if not policy.br_hm_112_room_capacity_available(room.capacity, room.occupancy):
        raise ValueError("No capacity")

    room.occupancy += 1
    return RoomAllocation(
        allocation_id=f"RA-{student_id}",
        student_id=student_id,
        room_id=room.room_id
    )


# =====================================================
# WF-104 — ROOM CHANGE
# =====================================================

def request_room_change(student_id: str, reason: str) -> RoomChangeRequest:
    return RoomChangeRequest(
        request_id=f"RC-{student_id}",
        student_id=student_id,
        reason=reason
    )


def approve_room_change(req: RoomChangeRequest,
                         caretaker_ok: bool, warden_ok: bool,
                         old_room: Room, new_room: Room) -> RoomAssignmentHistory:
    if not policy.br_hm_116_dual_approval_required(caretaker_ok, warden_ok):
        raise PermissionError("Dual approval required")

    old_room.occupancy -= 1
    new_room.occupancy += 1
    req.status = "APPROVED"

    return RoomAssignmentHistory(
        student_id=req.student_id,
        old_room=old_room.room_id,
        new_room=new_room.room_id
    )


# =====================================================
# WF-105 — FINE MANAGEMENT
# =====================================================

def impose_fine(role: str, student_id: str,
                amount: float, reason: str) -> Fine:
    if not policy.br_hm_012_authorized_roles_impose_fine(role):
        raise PermissionError("Unauthorized")

    if not policy.br_hm_013_fine_amount_positive(amount):
        raise ValueError("Invalid amount")

    return Fine(
        fine_id=f"FINE-{student_id}",
        student_id=student_id,
        amount=amount,
        reason=reason
    )


# =====================================================
# WF-106 — HOSTEL SETUP & STAFFING
# =====================================================

def create_hostel(admin_id: str, name: str,
                  hostel_type: str, address: str, capacity: int) -> Hostel:
    return Hostel(
        hostel_id=f"H-{name}",
        name=name,
        hostel_type=hostel_type,
        address=address,
        capacity=capacity
    )


def assign_staff(staff_id: str, hostel_id: str, role: str) -> StaffAssignment:
    return StaffAssignment(
        assignment_id=f"SA-{staff_id}-{hostel_id}",
        staff_id=staff_id,
        hostel_id=hostel_id,
        role=role
    )


# =====================================================
# WF-107 — SECURITY
# =====================================================

def assign_guard(guard_id: str, name: str, phone: str) -> Guard:
    return Guard(guard_id=guard_id, name=name, phone=phone, status="ACTIVE")


def log_incident(description: str, severity: str) -> IncidentReport:
    if not policy.br_hm_028_incident_must_have_severity(severity):
        raise ValueError("Severity required")

    return IncidentReport(
        report_id=f"INC-{datetime.now().timestamp()}",
        description=description,
        severity=severity
    )


# =====================================================
# WF-108 — VISITOR
# =====================================================

def request_visit(visit_date: date) -> VisitRequest:
    return VisitRequest(
        request_id=f"VR-{visit_date}",
        visit_date=visit_date
    )


def log_visit(entry_time: datetime, exit_time: Optional[datetime]) -> VisitLog:
    return VisitLog(
        log_id=f"VL-{entry_time.timestamp()}",
        entry_time=entry_time,
        exit_time=exit_time
    )


# =====================================================
# WF-109 — ROOM VACATION
# =====================================================

def request_vacation(student_id: str, vacation_date: date) -> RoomVacationRequest:
    if not policy.br_hm_018_vacation_date_future(vacation_date, date.today()):
        raise ValueError("Date must be future")

    return RoomVacationRequest(
        request_id=f"RV-{student_id}",
        student_id=student_id,
        vacation_date=vacation_date
    )


def perform_clearance(student_id: str, cleared_by: str,
                      pending_dues: float, inventory_clear: bool) -> ClearanceRecord:
    if not policy.br_hm_016_clearance_requires_no_dues(pending_dues, inventory_clear):
        raise ValueError("Clearance failed")

    return ClearanceRecord(
        record_id=f"CLR-{student_id}",
        student_id=student_id,
        cleared_by=cleared_by
    )


# =====================================================
# WF-110 — NOTICE
# =====================================================

def create_notice(title: str, description: str, priority: str,
                  title_len: int, desc_len: int) -> Notice:
    if not policy.br_hm_029_notice_length_valid(title_len, desc_len):
        raise ValueError("Invalid content length")

    return Notice(
        notice_id=f"N-{datetime.now().timestamp()}",
        title=title,
        description=description,
        priority=priority
    )


# =====================================================
# WF-111 — REPORTS
# =====================================================

def generate_report(role: str, report_type: str,
                    params: ReportParameters) -> Report:
    if not policy.br_hm_040_authorized_generate_reports(role):
        raise PermissionError("Unauthorized")

    return Report(
        report_id=f"R-{datetime.now().timestamp()}",
        report_type=report_type
    )


def archive_report(report: Report) -> ArchivedReport:
    if not policy.br_hm_050_reports_archived():
        raise RuntimeError("Archival failed")

    report.status = "ARCHIVED"
    return ArchivedReport(report_id=report.report_id)


# =====================================================
# WF-112 — GUEST ROOM
# =====================================================

def request_guest_room(student_id: str) -> GuestRoomBooking:
    return GuestRoomBooking(
        booking_id=f"GB-{student_id}",
        student_id=student_id
    )


# =====================================================
# WF-113 — EXTENDED STAY
# =====================================================

def apply_extended_stay(student_id: str, reason: str,
                        academic_standing: str, faculty_ok: bool) -> ExtendedStayApplication:
    if not policy.br_hm_061_extended_stay_eligibility(academic_standing, faculty_ok):
        raise ValueError("Not eligible")

    return ExtendedStayApplication(
        application_id=f"ES-{student_id}",
        student_id=student_id,
        reason=reason
    )
