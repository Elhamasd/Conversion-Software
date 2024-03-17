

class CHECK_PARAMETER():
        def __init__(self) -> None:
            self._file_input=""
            self._r_button=""
            self._file_name=""
            self._file_out=""
        @property
        def file_input(self):
            return self._file_input
        @file_input.setter
        def file_input(self, a):
            self._file_input = a  
        @property
        def r_button(self):
            return self._r_button
        @r_button.setter
        def r_button(self, a):
            self._r_button = a 

        @property
        def file_name(self):
            return self._file_name
        @file_name.setter
        def file_name(self, a):
            self._file_name = a  


        @property
        def file_out(self):
            return self._file_out
        @file_out.setter
        def file_out(self, a):
            self._file_out = a  