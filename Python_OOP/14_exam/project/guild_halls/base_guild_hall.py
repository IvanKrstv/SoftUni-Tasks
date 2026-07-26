from abc import ABC, abstractmethod

from project.guild_members.base_guild_member import BaseGuildMember


class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members: list[BaseGuildMember] = []
        
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, value: str):
        trimmed = value.strip()
        if len(trimmed) < 2 or not trimmed.replace(" ", "").isalpha():
            raise ValueError("Guild hall alias is invalid!")
        self.__alias = trimmed

    @property
    @abstractmethod
    def max_member_count(self):
        pass

    def calculate_total_gold(self):
        total_gold = sum([member.gold for member in self.members])

        return total_gold

    def status(self):
        info = f"Guild hall: {self.alias}; Members: "
        info += " *".join(member.tag for member in sorted(self.members, key=lambda x: x.tag)) if self.members else "N/A"
        info += f"; Total gold: {self.calculate_total_gold()}"

        return info

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass