import datetime # imports datetime module: used to __generate_id()
import string # imports string module: used to __generate_id()

class Patient(object):
    """Class for creating instances of Patients."""

    def __init__(self, name, allergies, bed=None):
        """Constructor method for (creates) new Patients.

        Parameters:
        --name: Name of patient (no default setting).
        --allergies: Patient allergies (no default setting).
        --bed: Bed number of patient (default=None).

        Notes: 'id' field is also part of `Patient` instance, and
        is generated at random upon instance creation.
        """
        self.id = self.__generate_id() # creates a random id
        self.name = name
        self.allergies = allergies
        self.bed = bed
        return None # __init__ method must return `None`

    def __generate_id(self):
        """Generates `id`s for new patients."""

        # Takes a timestamp (including milliseconds), converts it to string, removes all punctuation.
        unique_id = str(datetime.datetime.utcnow()).translate(None, string.punctuation).replace(" ", "")
        return unique_id

class Hospital(object):
    """Class for creating instances of Hospitals."""

    def __init__(self, name, capacity):
        """Constructor method for (creats) new Hospitals.

        Parameters:
        --name: Name of hospital.
        --capacity: Max capacity of patients as an integer.
        """

        self.patients = []
        self.name = name
        self.capacity = capacity
        return None

    def admit(self, patient, bed_num):
        """Add a `Patient` to the Hospital.

        Parameters:
        --patient: Patient object to add to `Hospital`.
        --bed_num: Bed number to assign to Patient object.
        """

        # Check if patients are at capacity:
        if len(self.patients) >= self.capacity:
            print "Cannot admit patient -- Hospital already @ max capacity of: {}".format(len(self.patients))
            return "Hospital is full. Cannot admit Patient."
        # Otherwise, admit patient:
        else:
            # Assign bed to patient, add to hospital:
            patient.bed = bed_num # assign bed number to `Patient`
            self.capacity = self.capacity - 1
            self.patients.append(patient) # add Patient to Hospital `Patients` list
            print "Patient has been admitted to bed: {}".format(patient.bed)
            return self, "Patient has been admitted to bed: {}".format(patient.bed)

    def discharge(self, patient_object):
        """Remove a `Patient` from the Hospital.

        Parameters:
        --patient_object: Patient object of whom to remove.
        """

        # Loop through Patients:
        for patient in self.patients:
            # If patient matches `patient_object`:
            if patient == patient_object:
                # Set bed number for `Patient` to none:
                patient.bed = None
                # Adjust Hospital Capacity:
                self.capacity = self.capacity + 1
                # Delete `Patient` based on idx:
                del self.patients[self.patients.index(patient)]
                print "Patient has been discharged."
                return self, "Patient has been discharged."

# Create Instances of Patients:
tim = Patient("Tim Knab", "No Allergies.")
julianna = Patient("Julianna Giles", "No Allergies.")

# Print Info for Each Patient:
print "#------ PATIENT INFO ------#"
print "ID: ", tim.id
print "NAME: ", tim.name
print "ALLERGIES: ", tim.allergies
print "BED: ", tim.bed

print "\n" # insert blank line for printing

print "#------ PATIENT INFO ------#"
print "ID: ", julianna.id
print "NAME: ", julianna.name
print "ALLERGIES: ", julianna.allergies
print "BED: ", julianna.bed

# Create Instance of Hospital:
lakeside = Hospital("Lakewood", 1)

print "\n" # insert blank line for printing

# Print Hospital Instance Information:
print "#******** HOSPITAL INFO ********#"
print "PATIENTS: ", lakeside.patients
print "NAME: ", lakeside.name
print "CAPACITY: ", lakeside.capacity

# Test Hospital `admit()` Instance Methods:
lakeside.admit(tim, 1)
lakeside.admit(julianna, 2)

print "\n" # insert blank line for printing

# See If Our Hospital Info Has Changed:
print "#******** HOSPITAL INFO ********#"
print "PATIENTS: ", lakeside.patients # should now contain Patient object
print "NAME: ", lakeside.name
print "CAPACITY: ", lakeside.capacity # should be decremented

# Test Hospital `discharge()` Instance Methods:
lakeside.discharge(tim)

print "\n" # insert blank line for printing

# See If Our Hospital Info Has Changed:
print "#******** HOSPITAL INFO ********#"
print "PATIENTS: ", lakeside.patients
print "NAME: ", lakeside.name
print "CAPACITY: ", lakeside.capacity
