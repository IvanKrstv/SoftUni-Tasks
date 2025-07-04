class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info = (f'Name: {self.name}\n'
                f'Guild: {self.guild}\n'
                f'HP: {self.hp}\n'
                f'MP: {self.mp}\n')
        for skill, mc in self.skills.items():
            info += f'==={skill} - {mc}\n'
        return info
