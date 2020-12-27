#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
from stuff.game_app import GameOfLife


@pytest.fixture
def tgame(scope='session'):
    return GameOfLife()


def test_first_test():
    assert 2 + 2 == 4


def test_game_init(tgame):
    biggerthans = [(1, tgame.min_life, tgame.max_life, 8), (0, tgame.initial_births, 2500)]

    for relation in biggerthans:
        r = list(relation)
        sorted_r = sorted(relation)
        assert r == sorted_r, 'one of the main values defined is not valid'


test_cases = [(2, 3, 3, 100), (1, 2, 2, 100), (2, 3, 3, 2), (2, 3, 3, 500)]


@pytest.mark.parametrize('min_for_life, max_for_life, birth, initial_births', test_cases)
def test_game_over(min_for_life, max_for_life, birth, initial_births):

    # make sure game over is declared on time.

    tgame = GameOfLife(min_for_life, max_for_life, birth, initial_births)
    tgame.run_by_rounds()
    if tgame.game_over:
        assert tgame.get_board() == [[0 for j in range(50)] for i in range(50)]
    else:
        assert tgame.get_board() != [[0 for j in range(50)] for i in range(50)]
