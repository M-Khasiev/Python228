import csv
import os


class ModelInstance:
    def __init__(self):
        self.file_data = 'cinema.csv'
        self.data_dict = self.load_data()

    def model_data_recording(self, d):
        self.data_dict[d["Название фильма"]] = d

    def model_available_data(self):
        return self.data_dict

    def model_certain_movie(self, cinema):
        m = self.data_dict[cinema]
        return m

    def model_delete_movie(self, cinema):
        return self.data_dict.pop(cinema)

    def load_data(self):
        if os.path.exists(self.file_data):
            lst = list()
            with open(self.file_data, 'r') as rf:
                file_reader1 = csv.reader(rf, delimiter=";")
                for i in file_reader1:
                    lst.append(i)
                if len(lst) > 1:
                    with open(self.file_data, 'r') as f:
                        file_reader2 = csv.DictReader(f, delimiter=";")
                        d = dict()
                        for i in file_reader2:
                            d[i["Название фильма"]] = i
                        return d
                else:
                    return dict()
        else:
            return dict()

    def save_data(self):
        with open(self.file_data, 'w') as f:
            names = ["Название фильма", "Жанр", "Режиссер", "Год выпуска", "Длительность", "Студия", "Актёры"]
            wr = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
            wr.writeheader()
            for i in self.data_dict.values():
                wr.writerow(i)
