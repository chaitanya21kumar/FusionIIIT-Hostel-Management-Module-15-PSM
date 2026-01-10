"""
views.py
Boundary Layer — Hostel Management PSM
"""

from datetime import date, datetime

from .services import (
    apply_leave,
    submit_complaint,
    impose_fine,
    create_notice,
    generate_report,
)
from .serializers import (
    leave_request_to_dict,
    complaint_to_dict,
    fine_to_dict,
    notice_to_dict,
    report_to_dict,
)


# -------------------------
# WF-101 — Leave Boundary
# -------------------------

def submit_leave_view(payload: dict):
    leave = apply_leave(
        student_id=payload["student_id"],
        hostel_status=payload["hostel_status"],
        start_date=payload["start_date"],
        end_date=payload["end_date"],
        reason=payload["reason"],
        docs_attached=payload["docs_attached"],
    )
    return leave_request_to_dict(leave)


# -------------------------
# WF-102 — Complaint Boundary
# -------------------------

def submit_complaint_view(payload: dict):
    complaint = submit_complaint(
        student_id=payload["student_id"],
        hostel_status=payload["hostel_status"],
        category=payload["category"],
        description=payload["description"],
    )
    return complaint_to_dict(complaint)


# -------------------------
# WF-105 — Fine Boundary
# -------------------------

def impose_fine_view(payload: dict):
    fine = impose_fine(
        role=payload["role"],
        student_id=payload["student_id"],
        amount=payload["amount"],
        reason=payload["reason"],
    )
    return fine_to_dict(fine)


# -------------------------
# WF-110 — Notice Boundary
# -------------------------

def create_notice_view(payload: dict):
    notice = create_notice(
        title=payload["title"],
        description=payload["description"],
        priority=payload["priority"],
        title_len=len(payload["title"]),
        desc_len=len(payload["description"]),
    )
    return notice_to_dict(notice)


# -------------------------
# WF-111 — Report Boundary
# -------------------------

def generate_report_view(payload: dict):
    report = generate_report(
        role=payload["role"],
        report_type=payload["report_type"],
        params=payload["params"],
    )
    return report_to_dict(report)
