class Warranty:
    """this is class documentation"""

    def __init__(self):
        self.warranties = {}

    def __iter__(self):
        return WarrantyIterator(self.warranties)

    def add_car(self, serial_number: int, date: str):
        """this will add a new car to the list of warranties"""
        date_object = datetime.datetime.strptime(date, '%d %b %Y %H:%M:%S')
        self.warranties.update({serial_number: date_object})

    def get_expired_warranties(self):
        now = datetime.datetime.now()
        for serial, date in self.warranties.items():
            result = now - date
            if result.days / 365 > 3:
                print(serial)


class WarrantyIterator:

    def __init__(self, warranty_data: dict):
        self.warranty_data = warranty_data

    def __iter__(self):
        return self

    def __next__(self):
        if not self.warranty_data:
            raise StopIteration
        now = datetime.datetime.now()
        for serial, date in self.warranty_data.copy().items():
            result = now - date
            if result.days / 365 < 3:
                r = (serial, result)
                del self.warranty_data[serial]
                return r
            else:
                del self.warranty_data[serial]
                continue


w = Warranty()
w.add_car(1588, '28 Jan 2019 10:30:32')
w.add_car(1598, '28 Jan 2022 10:30:32')
print(w.warranties)
w.get_expired_warranties()
with open('exemple.txt', 'w') as file:
    for serial in w:
        file.write(str(serial) + '\n')