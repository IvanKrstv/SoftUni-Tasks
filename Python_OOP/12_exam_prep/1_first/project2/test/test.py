from project.soccer_player import SoccerPlayer
from unittest import TestCase, main

class SoccerPlayerTests(TestCase):
    def test_init(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")

        self.assertEqual("test_name", player.name)
        self.assertEqual(20, player.age)
        self.assertEqual(300, player.goals)
        self.assertEqual("PSG", player.team)
        self.assertEqual({}, player.achievements)

    def test_name_less_or_five_characters_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("test", 20, 300, "PSG")
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("test5", 20, 300, "PSG")
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_age_less_than_16_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("test_name", 15, 300, "PSG")
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_goals_less_than_0(self):
        player = SoccerPlayer("test_name", 20, -2, "PSG")

        self.assertEqual(0, player.goals)

    def test_team_invalid_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("test_name", 20, 300, "Uo")
        self.assertEqual(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!", str(ex.exception))

    def test_change_team_invalid_team(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")

        result = player.change_team("uo")

        self.assertEqual("Invalid team name!", result)

    def test_change_team(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")

        result = player.change_team("Barcelona")

        self.assertEqual("Barcelona", player.team)
        self.assertEqual("Team successfully changed!", result)

    def test_add_new_achievement_not_in_achievements(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")

        result = player.add_new_achievement("UCL")

        self.assertEqual({"UCL": 1}, player.achievements)
        self.assertEqual(f"UCL has been successfully added to the achievements collection!", result)

    def test_add_new_achievement(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")
        player.achievements = {"UCL": 2}

        result = player.add_new_achievement("UCL")

        self.assertEqual({"UCL": 3}, player.achievements)
        self.assertEqual(f"UCL has been successfully added to the achievements collection!", result)

    def test_lt_less_goals(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")
        player2 = SoccerPlayer("other_name", 20, 400, "PSG")

        result = player < player2

        self.assertEqual( "other_name is a top goal scorer! S/he scored more than test_name.", result)

    def test_lt_more_goals(self):
        player = SoccerPlayer("test_name", 20, 300, "PSG")
        player2 = SoccerPlayer("other_name", 20, 200, "PSG")

        result = player < player2

        self.assertEqual("test_name is a better goal scorer than other_name.", result)


if __name__ == '__main__':
    main()