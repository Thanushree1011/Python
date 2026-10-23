from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class for a person."""

    @abstractmethod
    def get_gender(self):
        """Return the gender label for this implementation."""
        pass


class Male(Person):
    """Male implementation of Person."""

    def get_gender(self):
        return "Male"


class Female(Person):
    """Female implementation of Person."""

    def get_gender(self):
        return "Female"


if __name__ == "__main__":
    people = [Male(), Female()]

    for person in people:
        print(person.get_gender())