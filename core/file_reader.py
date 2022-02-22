from abc import abstractmethod


class FileReader:
    @abstractmethod
    def read(self, filename: str) -> list:
        """
        Get list of words data from file.
        @param filename: path to the file
        @return string values of file
        """
        pass


class TxtFileReader(FileReader):
    def read(self, filename: str) -> list:
        try:
            with open(filename, 'r') as file:
                return file.read().splitlines()
        except Exception as err:
            raise err


file_reader = TxtFileReader()
