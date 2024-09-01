
from doctor import Doctor
from patient import Patient


def display_person_details(person):
    print(person.get_details())


patient = Patient(name='Omer' , age=30 , medical_history='Hypertension')
doctor = Doctor(name='Dr. Hesham' , age=45 , specialty='Cardiology')

display_person_details(patient)
display_person_details(doctor)