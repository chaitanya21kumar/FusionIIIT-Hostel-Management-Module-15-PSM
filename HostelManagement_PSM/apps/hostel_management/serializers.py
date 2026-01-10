"""
serializers.py
DTO Mappers — Hostel Management PSM
"""

def leave_request_to_dict(leave):
    return {
        "request_id": leave.request_id,
        "student_id": leave.student_id,
        "start_date": leave.start_date,
        "end_date": leave.end_date,
        "status": leave.status,
        "remarks": leave.remarks,
    }


def complaint_to_dict(complaint):
    return {
        "complaint_id": complaint.complaint_id,
        "student_id": complaint.student_id,
        "category": complaint.category,
        "description": complaint.description,
        "status": complaint.status,
    }


def fine_to_dict(fine):
    return {
        "fine_id": fine.fine_id,
        "student_id": fine.student_id,
        "amount": fine.amount,
        "reason": fine.reason,
        "status": fine.status,
    }


def notice_to_dict(notice):
    return {
        "notice_id": notice.notice_id,
        "title": notice.title,
        "description": notice.description,
        "priority": notice.priority,
        "status": notice.status,
    }


def report_to_dict(report):
    return {
        "report_id": report.report_id,
        "type": report.type,
        "status": report.status,
        "generated_at": report.generated_at,
    }
