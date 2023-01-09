from unittest import TestCase, main
import swgoh_comlink


class TestGetGuildByCriteria(TestCase):
    def test_get_guild_by_criteria(self):
        """
        Test that guild data can be retrieved from game server correctly
        """
        comlink = swgoh_comlink.SwgohComlink()
        p = comlink.get_guilds_by_criteria(search_criteria={"minGuildGalacticPower": 490000000})
        self.assertTrue('guild' in p.keys())


if __name__ == '__main__':
    main()
