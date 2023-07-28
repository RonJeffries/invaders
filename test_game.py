from game import Game


class TestGame:
    def test_main_loop(self):
        game = Game(testing=True)
        assert game.main_loop() == "done"
