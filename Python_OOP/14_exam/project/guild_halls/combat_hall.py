from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_members.warrior import Warrior


class CombatHall(BaseGuildHall):
    @property
    def max_member_count(self):
        return 3

    def increase_gold(self, min_skill_level_value: int):
        for member in self.members:
            if isinstance(member, Warrior) and member.skill_level >= min_skill_level_value:
                member.gold += 300
