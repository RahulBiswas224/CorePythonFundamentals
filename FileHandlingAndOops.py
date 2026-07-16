# FileHandlingAndOops.py

# I. & II. File Handling
def manageFiles():
    # Text File
    with open('std_rec.txt', 'w') as f:
        f.write("Name: John, Roll: 101, Marks: 95")
    
    # Binary File
    with open('data.bin', 'wb') as f:
        f.write(b'\x00\x01\x02\x03')
    with open('data.bin', 'rb') as f:
        print(f"Binary Content: {f.read()}")

# III. Classes and Objects
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# IV. Inheritance
class Result(Student):
    def showResult(self, marks):
        print(f"Student: {self.name}, Roll: {self.roll}, Marks: {marks}")
