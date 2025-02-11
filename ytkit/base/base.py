from abc import ABC, abstractmethod


class BaseGet(ABC):
    @abstractmethod
    def get(self):
        """
        Abstract method to be implemented by all classes inheriting from ytkit.baseGet.
        """
        pass
