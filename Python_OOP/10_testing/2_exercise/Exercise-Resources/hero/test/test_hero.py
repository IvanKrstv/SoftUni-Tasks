from unittest import TestCase, main
from project.hero import Hero

class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("test", 10, 100, 50)
        self.enemy = Hero("other", 10, 100, 40)

    def test_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(50, self.hero.damage)

    def test_battle_against_itself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("test", 10, 100, 40))
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_or_less_health(self):
        self.hero.health -= 100
        self.assertEqual(0, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health -= 1
        self.assertEqual(-1, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_with_zero_or_less_health(self):
        self.enemy.health -= 100
        self.assertEqual(0, self.enemy.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

        self.enemy.health -= 1
        self.assertEqual(-1, self.enemy.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_both_with_zero_or_less_health(self):
        # both negative health
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

        # both zero health
        hero = Hero("test", 10, 400, 50)
        enemy = Hero("other", 10, 500, 40)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

        # hero zero, enemy negative
        hero = Hero("test", 10, 400, 50)
        enemy = Hero("other", 10, 100, 40)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

        # hero negative, enemy zero
        hero = Hero("test", 10, 100, 50)
        enemy = Hero("other", 10, 500, 40)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_hero_win(self):
        hero = Hero("test", 10, 1000, 50)
        enemy = Hero("other", 10, 100, 40)
        result = hero.battle(enemy)
        self.assertEqual(11, hero.level)
        self.assertEqual(605, hero.health)
        self.assertEqual(55, hero.damage)
        self.assertEqual("You win", result)

        hero = Hero("test", 10, 1000, 50)
        enemy = Hero("other", 10, 500, 40)
        result = hero.battle(enemy)
        self.assertEqual(11, hero.level)
        self.assertEqual(605, hero.health)
        self.assertEqual(55, hero.damage)
        self.assertEqual("You win", result)

    def test_battle_hero_lose(self):
        hero = Hero("test", 10, 100, 50)
        enemy = Hero("other", 10, 5000, 40)
        result = hero.battle(enemy)
        self.assertEqual(11, enemy.level)
        self.assertEqual(4505, enemy.health)
        self.assertEqual(45, enemy.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        self.assertEqual(f"Hero {'test'}: {10} lvl\n" 
               f"Health: {100}\n" 
               f"Damage: {50}\n", str(self.hero))

if __name__ == '__main__':
    main()