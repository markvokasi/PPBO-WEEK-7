class Passenger:
    TITLES = ("Mr", "Mrs", "Ms")  # Class Attribute

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title  # Instance Attribute
        self.fname = fname  # Instance Attribute
        self.lname = lname  # Instance Attribute

# Pembuatan Objek
p1 = Passenger("Mr", "Kiewlamphone", "Souvanlith")
# Mengakses class attribute dari object
print(p1.TITLES)
# Mengakses class attribute dari kelas
print(Passenger.TITLES)
# Mengakses instance attribute dari object
print(p1.title)
