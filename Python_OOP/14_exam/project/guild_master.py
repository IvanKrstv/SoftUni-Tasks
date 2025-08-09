from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.base_guild_member import BaseGuildMember
from project.guild_members.warrior import Warrior
from project.guild_members.mage import Mage

class GuildMaster:
    VALID_MEMBER_TYPES = {"Warrior": Warrior, "Mage": Mage}
    VALID_HALL_TYPES = {"CombatHall": CombatHall, "MagicTower": MagicTower}

    def __init__(self):
        self.members: list[BaseGuildMember] = []
        self.guild_halls: list[BaseGuildHall] = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        if member_type not in self.VALID_MEMBER_TYPES:
            raise ValueError("Invalid member type!")

        if member_tag in [member.tag for member in self.members]:
            raise ValueError(f"{member_tag} has already been added!")

        member = self.VALID_MEMBER_TYPES[member_type](tag=member_tag, gold=member_gold)
        self.members.append(member)
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        if guild_hall_type not in self.VALID_HALL_TYPES:
            raise ValueError("Invalid guild hall type!")

        if guild_hall_alias in [hall.alias for hall in self.guild_halls]:
            raise ValueError(f"{guild_hall_alias} has already been added!")

        hall = self.VALID_HALL_TYPES[guild_hall_type](alias=guild_hall_alias)
        self.guild_halls.append(hall)
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = next((hall for hall in self.guild_halls if hall.alias == guild_hall_alias), None)
        if not guild_hall:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        member = next((member for member in self.members if isinstance(member, self.VALID_MEMBER_TYPES[member_type])), None)
        if not member:
            raise ValueError("No available members of the type!")

        if len(guild_hall.members) >= guild_hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        guild_hall.members.append(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."

    @staticmethod
    def practice_members(guild_hall: BaseGuildHall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()

        total_skill_level = sum(m.skill_level for m in guild_hall.members)
        return f"{guild_hall.alias} members have {total_skill_level} total skill level after {sessions_number} practice session/s."

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = next((member for member in guild_hall.members if member.tag == member_tag), None)
        if not member or member.skill_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for guild in self.guild_halls:
            guild.increase_gold(min_skill_level_value)

        sorted_guilds = list(sorted(self.guild_halls, key=lambda x: (-len(x.members), x.alias)))

        info = (f"<<<Guild Updated Status>>>\nUnassigned members count: {len(self.members)}\n"
                f"Guild halls count: {len(self.guild_halls)}\n")
        for guild in sorted_guilds:
            info += f">>>{guild.status()}\n"

        return info.strip()

# Create an instance of the Guild Master
manager = GuildMaster()

# Add members (warriors & mages)
print(manager.add_member("Warrior", "W02345", 100))
print(manager.add_member("Warrior", "12W34", 200))
print(manager.add_member("Warrior", "789123W", 250))
print(manager.add_member("Warrior", "WW45678999", 150))
print(manager.add_member("Mage", "M321654", 300))
print(manager.add_member("Mage", "654M3211", 320))
print(manager.add_member("Mage", "334654M", 350))
print(manager.add_member("Mage", "MM034654", 400))
print()

# Add guild halls
print(manager.add_guild_hall("MagicTower", "Silver Tower"))
print(manager.add_guild_hall("CombatHall", "Iron Bastion"))
print(manager.add_guild_hall("CombatHall", "Dragon Watch"))
print()

# Assign members to guild halls
print(manager.assign_member("Silver Tower", "Warrior"))
print(manager.assign_member("Silver Tower", "Mage"))
print(manager.assign_member("Silver Tower", "Mage"))
print(manager.assign_member("Dragon Watch", "Mage"))
print(manager.assign_member("Dragon Watch", "Warrior"))
print(manager.assign_member("Dragon Watch", "Warrior"))
print(manager.assign_member("Dragon Watch", "Warrior"))
print()

# Conduct practice sessions
print(manager.practice_members(manager.guild_halls[0], 0))
print(manager.practice_members(manager.guild_halls[0], 1))
print(manager.practice_members(manager.guild_halls[0], 2))
print(manager.practice_members(manager.guild_halls[0], 3))
print(manager.practice_members(manager.guild_halls[0], 5))
print(manager.practice_members(manager.guild_halls[1], 1))
print(manager.practice_members(manager.guild_halls[1], 0))
print(manager.practice_members(manager.guild_halls[2], 1))
print()

# Unassign a member
print(manager.unassign_member(manager.guild_halls[2], "334654M"))
print(manager.unassign_member(manager.guild_halls[0], "W02345"))
print(manager.guild_halls[0].members[0].tag, manager.guild_halls[0].members[0].skill_level)
print(manager.unassign_member(manager.guild_halls[0], "111111"))
print(manager.unassign_member(manager.guild_halls[1], "WW45678999"))
print()

# Perform a guild-wide update
print(manager.guild_update(8))
print()

# Check members gold after the update
print(manager.guild_halls[0].members[0].gold)
print(manager.guild_halls[0].members[1].gold)
print(manager.guild_halls[0].members[2].gold)
print()
print(manager.guild_halls[2].members[0].gold)
print(manager.guild_halls[2].members[1].gold)
print()
print(manager.members[0].gold)
print(manager.members[1].gold)
print(manager.members[2].gold)
