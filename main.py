class School:
    def __init__(self, name, level, numberOfStudents):
        self._name = name
        self._level = level
        self._numberOfStudents = numberOfStudents

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def numberOfStudents(self):
        return self._numberOfStudents

    @numberOfStudents.setter
    def numberOfStudents(self, value):
        self._numberOfStudents = value

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__() + f" Pickup Policy: {self.pickupPolicy}"


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        return super().__repr__() + f" Sports Teams: {', '.join(self.sportsTeams)}"


# Example usage:
primary_school = PrimarySchool(name="Primary School", numberOfStudents=300, pickupPolicy="After-school pickup")
print(primary_school)
print("Pickup Policy:", primary_school.get_pickupPolicy())

high_school = HighSchool(name="High School", numberOfStudents=1000, sportsTeams=["Football", "Basketball", "Soccer"])
print(high_school)
print("Sports Teams:", high_school.get_sportsTeams())
