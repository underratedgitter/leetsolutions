from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_count = Counter(hand)
        sorted_hand = sorted(hand_count.keys())

        for card in sorted_hand:
            if hand_count[card] > 0:
                count = hand_count[card]
                for next_card in range(card, card + groupSize):
                    if next_card not in hand_count or hand_count[next_card] < count:
                        return False
                    hand_count[next_card] -= count

        return True