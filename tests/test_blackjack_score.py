from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

#@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = [3, 4, 'King']
  score = blackjack_score(hand)
  assert score == 17

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = [9, 'Ace']
  score = blackjack_score(hand)
  assert score == 20


#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = ["King",2, 'Ace']
  score = blackjack_score(hand)
  assert score == 13

#pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = ['$']
  score = blackjack_score(hand)
  assert score == "Invalid"


#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [1,2,3,4,5,6]
  score = blackjack_score(hand)
  assert score == "Invalid"

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [5,7,'King']
  score = blackjack_score(hand)
  assert score == "Bust"

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ['Ace','Ace','King']
  score = blackjack_score(hand)
  assert score == 12

#@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    hand = ['Ace','Ace','Ace','Ace']
    score = blackjack_score(hand)
    assert score == 14