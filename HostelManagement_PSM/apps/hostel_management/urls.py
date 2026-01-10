"""
urls.py
Logical Endpoint Mapping — Hostel Management PSM
"""

URLS = {
    # WF-101
    "POST /leave/apply": "submit_leave_view",

    # WF-102
    "POST /complaint/submit": "submit_complaint_view",

    # WF-105
    "POST /fine/impose": "impose_fine_view",

    # WF-110
    "POST /notice/create": "create_notice_view",

    # WF-111
    "POST /report/generate": "generate_report_view",
}
