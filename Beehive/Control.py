
# Created by Jake Stephens


class Control():


    def __init__(self, frame):
        self.__frame = frame


    def clear(self):
        self.__frame.current_entry.delete("0", "end")
        self.__frame.target_entry.delete("0", "end")
        self.__frame.date_entry.delete("0", "end")
        self.__frame.text_field["state"] = "normal"
        self.__frame.text_field.delete("1.0", "end")
        self.__frame.text_field["state"] = "disabled"


    def cancel(self):
        print("TODO: Control.cancel()")


    def confirm(self):
        print("TODO: Control.confirm()")


    def archive(self):
        print("TODO: Control.archive()")


    def __my_private_method(self):
        print("NODO")