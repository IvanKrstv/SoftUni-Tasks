from project.id_mixin import IDMixin


class ExercisePlan(IDMixin):
    def __init__(self, trainer_id: int, equipment_id: int, duration: int ):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration # in minutes
        self.id = self.get_next_id()
        self.increment_id()

    @classmethod
    def from_hours(cls, trainer_id:int, equipment_id:int, hours:int):
        return cls(trainer_id=trainer_id, equipment_id=equipment_id, duration=hours * 60)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"