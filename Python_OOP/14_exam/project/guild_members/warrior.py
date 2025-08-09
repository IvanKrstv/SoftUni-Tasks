from project.guild_members.base_guild_member import BaseGuildMember

class Warrior(BaseGuildMember):
    ROLE = "Warrior"
    SKILL_LEVEL = 2
    
    def __init__(self, tag: str, gold: int):
        super().__init__(tag=tag, gold=gold, role=self.ROLE, skill_level=self.SKILL_LEVEL)

    def practice(self):
        new_result = self.skill_level + 2
        if new_result > 10:
            self.skill_level = 10
        else:
            self.skill_level = new_result

