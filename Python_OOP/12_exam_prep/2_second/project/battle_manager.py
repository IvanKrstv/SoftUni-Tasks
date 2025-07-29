from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        valid_types = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}

        if zone_type not in valid_types:
            raise Exception("Invalid zone type!")

        for zone in self.zones:
            if zone.code == zone_code:
                raise Exception("Zone already exists!")

        zone = valid_types[zone_type](zone_code)
        self.zones.append(zone)

        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        valid_types = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

        if ship_type not in valid_types:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship = valid_types[ship_type](name, health, hit_strength)
        self.ships.append(ship)

        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        #if len(zone.ships) >= zone.volume:
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        zone_type = zone.__class__.__name__[:5]
        ship_type = ship.__class__.__name__[:5]

        if ship_type == zone_type:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((ship for ship in self.ships if ship.name == ship_name), None)

        if ship is None:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)

        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attackers = [ship for ship in zone.ships if ship.is_attacking]
        targets = [ship for ship in zone.ships if not ship.is_attacking]

        if not attackers or not targets:
            return "Not enough participants. The battle is canceled."

        attacker = attackers[0]
        max_strength = attacker.hit_strength
        for ship in attackers:
            if ship.hit_strength > max_strength:
                attacker = ship

        target = targets[0]
        max_health = target.health
        for ship in targets:
            if ship.health > max_health:
                target = ship

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        info = f"Available Battleships: {len(available_ships)}\n"
        if available_ships:
            info += f"#{', '.join([ship.name for ship in available_ships])}#\n"
        info += f"***Zones Statistics:***\nTotal Zones: {len(self.zones)}\n"
        info += '\n'.join([zone.zone_info() for zone in self.zones])

        return info



# Initialize the BattleManager
battle_manager = BattleManager()

# Add zones
print(battle_manager.add_zone("RoyalZone", "001"))
print(battle_manager.add_zone("PirateZone", "002"))
print()

# Add battleships
print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 80, 45))
print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
print(battle_manager.add_battleship("PirateBattleship", "PirateThree", 90, 90))
print()

# Retrieve battleships and zones
royal_zone = battle_manager.zones[0]
pirate_zone = battle_manager.zones[1]

royal_one = battle_manager.ships[0]
royal_two = battle_manager.ships[1]
pirate_one = battle_manager.ships[2]
pirate_two = battle_manager.ships[3]

# Add ships to zones
print(battle_manager.add_ship_to_zone(royal_zone, royal_one))
print(battle_manager.add_ship_to_zone(royal_zone, pirate_one))
print(battle_manager.add_ship_to_zone(pirate_zone, royal_two))
print(battle_manager.add_ship_to_zone(pirate_zone, pirate_two))
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalTwo"))
print(battle_manager.remove_battleship("Nonexistent"))
print()

# Start battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Start battle in PirateZone
print(battle_manager.start_battle(pirate_zone))
print()

# Start another battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Retrieve updated statistics
print(battle_manager.get_statistics())
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalThree"))
