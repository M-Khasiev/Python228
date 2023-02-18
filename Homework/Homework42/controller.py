from model import ModelInstance
from view import Interface


class Controller:
    def __init__(self):
        self.model_instance = ModelInstance()
        self.view_instance = Interface()

    def launch(self):
        while True:
            user_choice = self.view_instance.giving_choice()
            if user_choice == '1':
                self.model_instance.model_data_recording(self.view_instance.view_data_recording())
            elif user_choice == '2':
                self.view_instance.view_movie_available(self.model_instance.model_available_data())
            elif user_choice == '3':
                try:
                    cinema = self.model_instance.model_certain_movie(self.view_instance.view_watching_specific_movie())
                except KeyError:
                    self.view_instance.absense()
                else:
                    self.view_instance.movie_information(cinema)
            elif user_choice == '4':
                try:
                    cinema = self.model_instance.model_delete_movie(self.view_instance.view_delete_specific_movie())
                except KeyError:
                    self.view_instance.absense()
                else:
                    self.view_instance.view_delete_information_movie(cinema)
            elif user_choice == 'q':
                self.model_instance.save_data()
                self.view_instance.end_programm()
                break
            else:
                self.view_instance.input_error(user_choice)
