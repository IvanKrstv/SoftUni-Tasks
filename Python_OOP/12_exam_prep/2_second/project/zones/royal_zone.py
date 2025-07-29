from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        pirate_ships = [ship for ship in self.ships if isinstance(ship, PirateBattleship)]
        info = (f"@Royal Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Royal Zone: {len(self.ships)}, {len(pirate_ships)} out of them are Pirate Battleships.\n")
        if self.ships:
            info += f"#{', '.join([ship.name for ship in self.get_ships()])}#"

        return info.strip()