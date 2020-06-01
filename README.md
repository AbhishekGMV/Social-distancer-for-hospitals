### Description

Idea of this project is to avoid crowding of visitors in general ward, maintains hygiene and also avoids disturbing the other patient in any means. <br>
Following steps occur in the process: <br>
  • Receptionist maintains information of the in-patients of the hospital. <br/>
  • Visitor enquires the receptionist about the patient, If the patient is admitted. <br/>
  • Receptionist enquires visitor for necessary information. <br/>
  • Generates a QR code based on bed number of respected patient. <br/>
  • The copy of QR code is sent to user via mail(to **save paper**) or a hard copy will be given if visitor doesn't have a phone.<br> 
  • SMS will be sent to visitor’s phone number about the visiting time. <br/>
  • An access device is maintained at the entrance of the ward which scans the QR code. (But this was quite beyond scope of this             project, it involves programming of hardware like Arduino board and raspberry pi.) <br/>
  • Visitor will receive an automated call before 5 minutes of end of visiting time. <br/>
  
  
  
### Actors on the scene <br/>

•	Receptionist – Maintains record of patient, communicates to visitor for information and generates QR code and facilitates automated SMS and Call services <br/>
•	Visitor –   Enquires receptionist for details of patient and visits patient. <br/>


### Tech stack used <br/>

[Twilio Rest API](https://www.twilio.com/) <br/>

*Twilio SMS and call services* were utilized to alert user about visiting time to visitor. <br/>
The phone number has to be a Registered to Twilio account and obtain SID, token and a ‘from’ number (had to be provided as input to the program). <br/>


### Advantages <br/>
 Reduces paper work! (Eco-friendly) <br/>
	QR will be sent to visitor’s Mail ID. <br/>
	In worst case (visitor who doesn’t have a phone), Hard copy of QR code will be provided. <br/>

 Improves Quality of business <br>
 Helps improve Social distancing activity.<br>
	Technology helps reduce Man power. <br>
	Reduces cost of maintenance. <br>

### Instructions to run the program  <br/>

Program takes in following inputs upon running: <br/>
•	Number of patients to be registered and, <br/>
•	Name of the patient <br/>
•	Bed number <br/>
•	Status (0 - admitted or 1 - discharged) respectively  <br/>

Above input maintain Register of patients. Now the visitor enquires the receptionist about the patient, receptionist takes following input to check and facilitate the visit if patient is admitted. <br/>

•	Name of the patient  <br/>
•	Phone number  <br/>
•	SID, Authorization token and a from number (Twilio Account)  <br/>
•	Visiting time in minutes <br/>
