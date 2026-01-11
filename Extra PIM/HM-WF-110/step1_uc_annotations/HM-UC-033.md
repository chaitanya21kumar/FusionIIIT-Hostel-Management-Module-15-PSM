## **UC: HM-UC-033 – View and Store Notice**


* **M1:** Student logs into system  
  *(Boundary: LoginView)*

* **M2:** **System displays Notice Board**  
  *(Boundary: NoticeBoardView)*

* **M3:** **System retrieves active notices** relevant to student  
  *(Control: NoticeQueryController)* →  
  **Notice, NoticeTarget**  
  *(Entities)*  
  *(Business Rules: BR-HM-035, BR-HM-039)*

* **M4:** **Display notices ordered by priority and date**  
  *(Boundary: NoticeListView)*  
  *(Business Rule: BR-HM-035)*

* **M5:** **Student applies filters** (priority, date, read/unread)  
  *(Boundary: User Action)*

* **M6:** **Student selects a notice**  
  *(Boundary: User Action)*

* **M7:** **System displays full notice content**  
  *(Boundary: NoticeDetailView)* →  
  **Notice, Attachment**  
  *(Entities)*

* **M8:** **System marks notice as Read**  
  *(Control: NoticeTrackingController)* →  
  **NoticeReadStatus (studentId, noticeId, readAt)**  
  *(Entity)*

* **M9:** **Student downloads attachment (optional)**  
  *(Boundary: User Action)*  
  *(Business Rule: BR-HM-022)*

* **M10:** **System monitors notice expiry**  
  *(Control: NoticeExpiryScheduler)*  
  *(Business Rule: BR-HM-036)*

* **M11:** **System archives expired notices**  
  *(Control: NoticeArchiveController)* →  
  **ArchivedNotice**  
  *(Entity)*

**Result:** Student views notices; system maintains read tracking and archive.
