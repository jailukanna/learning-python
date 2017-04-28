# Assignment: Hospital
You're going to build a hospital with patients in it! Create a hospital class.

Before looking at the requirements below, think about what you might want each patient and hospital to be able to do.

# Patient
##  Attributes:
+ Id: an id number
+ Name
+ Allergies
+ Bed number: should be none by default

# Hospital
## Attributes:

+ Patients: an empty array
+ Name: hospital name
+ Capacity: an integer indicating the maximum number of patients the hospital can hold.

## Methods:

+ Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.

+ Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.

This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
