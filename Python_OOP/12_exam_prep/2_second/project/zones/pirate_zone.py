from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=8)

    def zone_info(self):
        royal_ships = [ship for ship in self.ships if isinstance(ship, RoyalBattleship)]
        info = (f"@Pirate Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Pirate Zone: {len(self.ships)}, {len(royal_ships)} out of them are Royal Battleships.\n")
        if self.ships:
            info += f"#{', '.join([ship.name for ship in self.get_ships()])}#"

        return info.strip()