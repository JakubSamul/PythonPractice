from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def voice(self):
        pass


class Text(ABC):
    @abstractmethod
    def text_message(self):
        pass


class Camera(ABC):
    @abstractmethod
    def photo(self):
        pass

    
class BestMobilePhoneEver(Phone, Text, Camera):
    def voice(self):
        # some code
        pass

    def text_message(self):
        # some code
        pass

    def photo(self):
        # some code
        pass


class OldSchoolMobilePhone(Phone, Text):
    def voice(self):
        # some code
        pass

    def text_message(self):
        # some code
        pass


class Pager(Text):
    def text_message(self):
        # some code
        pass