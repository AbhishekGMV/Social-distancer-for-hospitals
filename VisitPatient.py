from twilio.rest import Client
from pyqrcode import QRCode
import threading 
import sys
import twilio
import pyqrcode

def register_patient():
    """
    Maintains information of patients like name, bed number provided to them
    and whether or not the patient is still Admitted(1), or Discharged(0) in the hospital.
    """
    try:
        n = int(input("Number of patients: "))
        patient_info = []
        for each_patient in range(n):
            patient_name = input("Patient Name: ")
            bed_num = int(input("Bed Number: "))
            status = int(input("Status: "))
            if status == 1:
                status = 'ADMITTED'
            elif status == 0:
                status = 'DISCHARGED'
            else:
                print('Invalid input')
                sys.exit(0)
            print()
            patient_info.append([patient_name,bed_num,status])
        return patient_info

    except ValueError:
        print('Invalid input')
        sys.exit(0)

    except:
        print('Something went wrong!')
        sys.exit(0)

        
def receptionist(patient_details,visitor_name):
    """
    (patient's details list, visitor_name)
    Takes in the necessary information, generates a QR code based on the bed
    number of the patient and saves that as a .svg file by visitor name
    """
    try:
        for patient in patient_details:
            if patient_name in patient:
                bed_num = patient[-2]
                print("Please wait while your QR code is being generated...")
                generatedQR = pyqrcode.create(bed_num)
                print("QR code generated!")
                visitorQR = visitor_name + ".svg"
                generatedQR.svg(visitorQR,scale =  8)

    except ValueError:
        print('Invalid input')
        sys.exit(0)

    except:
        print("Couldn't generate the QR code!")
        sys.exit(0)
    
    
def send_SMS():
    """
    sends SMS to visitor number regarding visiting time information to Provided 'Registered' twilio account sid,
    authorization token.
    """
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            to = visitor_phno,    #Registered twilio account phone number
            from_=from_number,   
            body=f'Your visiting time of {count} mins has been started! You will get a voice-call alert before 5 mins of exit time'
        )
    except:
        print("SMS not sent! Please provide a registered twilio api account SID and token or check the format of phone number!")
        sys.exit(0)
        
        
def call_visitor():
    """
    Places a call to visitor's number regarding end of visiting time information to Provided 'Registered' twilio account sid,
    authorization token.
    """
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
                            url='https://demo.twilio.com/docs/voice.xml',
                            to=visitor_phno,  #Registered twilio account phone number
                            from_=from_number)
    except:
        print("Couldn't place the call, Please provide a registered twilio api account SID and token or check the format of phone number!")
        sys.exit(0)
        
               
if __name__ == '__main__':
    register = register_patient()
    print("Patients information updated!")
    print("Provide following information to enquire the receptionist about the patient")
    
try:
    patient_name = input("Name of patient: ")
    for each_patient in register:

        if patient_name in each_patient and  each_patient[-1]=="ADMITTED":

            visitor_name = input("Visitor name: ")
            visitor_phno = input("Visitor phone number(with country code): ")
            account_sid, auth_token = input("SID: "), input("Token: ")
            from_number = input("From number: ")
            receptionist(register, visitor_name)

        else:
            print("Sorry, no patient by name '{}' is admitted or has already been discharged!".format(patient_name))
            sys.exit(0)
            
    try:
        count = float(input("Visiting Time in minutes: "))
        timer = threading.Timer(count*60, call_visitor)
        timer.start()
        send_SMS()
        print("Timer started! SMS has been sent to visitor ")

    except ValueError:
        print("Invalid format, couldn't start timer!")

except ValueError:
    print("Invalid input")
