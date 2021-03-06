import csv


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:

    def __init__(self, filepath):
        self.data = []
        with open(filepath) as input_data:
            csv_data = csv.DictReader(input_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
