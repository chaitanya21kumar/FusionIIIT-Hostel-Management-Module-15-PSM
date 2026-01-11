## **UC: HM-UC-032 – Create and Publish Notice**

* **M1:** Open **Notice Creation Form**  
  *(Boundary: NoticeForm / View)*

* **M2:** **Enter notice details** – title, description  
  *(Boundary: User Action)* →  
  **Notice (title, description, priority, startDate, endDate, status)**  
  *(Entity: Attributes)*

* **M3:** **Upload attachments (optional)**  
  *(Boundary: User Action)* →  
  **Attachment (id, fileName, fileType, fileSize)**  
  *(Entity)*  
  *(Business Rule: BR-HM-022)*

* **M4:** **Select target audience** – hostel(s), rooms, or all students  
  *(Boundary: User Action)* →  
  **NoticeTarget (hostelId, scopeType)**  
  *(Entity)*  
  *(Business Rule: BR-HM-039)*

* **M5:** **Set notice priority** – Normal / Important / Urgent  
  *(Boundary: User Action)* →  
  **Notice.priority**  
  *(Entity Attribute)*  
  *(Business Rule: BR-HM-033)*

* **M6:** **Set display duration** – start date, end date  
  *(Boundary: User Action)* →  
  **Notice.startDate, Notice.endDate**  
  *(Entity Attributes)*

* **M7:** **Preview notice**  
  *(Boundary: NoticePreviewView)*

* **M8:** **Publish notice**  
  *(Boundary: User Action)* →  
  **Notice.status = Published**  
  *(Entity Attribute)*

* **M9:** **System validates notice content**  
  *(Control: NoticeValidationController)*  
  *(Business Rules: BR-HM-029, BR-HM-033)*

* **M10:** **System publishes notice**  
  *(Control: NoticePublishController)* →  
  Notice persisted in **NoticeRepository**

* **M11:** **System sends notifications**  
  *(Control: NotificationService)*  
  *(Business Rule: BR-HM-033)*

* **M12:** **Display success confirmation with Notice ID**  
  *(Boundary: ConfirmationView)*

**Result:** Notice becomes active and visible to students.
