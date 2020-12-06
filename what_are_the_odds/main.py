import random


def roll():
    return random.randint(0, 14)


def check_roll(num):
    if 1 <= num <= 7:
        # Red
        win = True
    else:
        win = False
    return win


def test_probability():
    win_count = 0
    total = 0
    while True:
        if check_roll(roll()):
            win_count += 1
        total += 1

        print(win_count, total)
        print(win_count / total)
        print()


def gamble(occur):
    starting_bal = 10
    bal = starting_bal
    starting_bet = 0.1
    bet = starting_bet
    bet_multiplier = 2

    longest_win_streak = 0
    win_streak = longest_win_streak
    longest_loss_streak = 0
    loss_streak = longest_loss_streak

    print("--------------------------------")
    print("Starting balance: " + str(bal))
    print("--------------------------------")
    print()
    print()
    print()

    for i in range(occur):
        print("--------------------------------")

        print("Betting: " + str(bet))

        # place bet, check if win
        if check_roll(roll()):
            loss_streak = 0
            win_streak += 1
            if win_streak > longest_win_streak:
                longest_win_streak = win_streak
            # win
            bal += bet * 2
            # reset to starting bet
            bet = starting_bet
            print("Win! New balance: " + str(bal))
            print()
        else:
            win_streak = 0
            loss_streak += 1
            if loss_streak > longest_loss_streak:
                longest_loss_streak = loss_streak
            # loss
            # subtract losings
            bal -= bet
            # double bet
            bet *= bet_multiplier
            print("Loss... New balance: " + str(bal))
        print("--------------------------------")
        print()
        print()

    print()
    print()
    print()
    print(f"Total winnings: ${bal - starting_bal}")
    print(
        f"Highest loss streak: {longest_loss_streak}, which is -${starting_bet * (2 ** longest_loss_streak)} for the final loss individually.")
    print(f"Highest win streak: {longest_win_streak}, which is +${starting_bet * longest_win_streak}")
    return bal - starting_bal


# 7 / 15 chance to win on red
# 7 / 15 chance to win on black
# 1 / 15 chance to win on green
def run_test(trials, games):
    total_winnings = 0
    trials_completed = 0
    for i in range(trials):
        winnings = gamble(games)
        total_winnings += winnings
        trials_completed += 1
    print()
    print()
    print()
    print(f"Average winnings across {trials} trials of {games} games per trial: ${total_winnings / trials_completed}")


run_test(1, 10)
