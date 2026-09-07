"""
Weighted Borda Count Preference Aggregator Skill Client
Pure Python Standard Library implementation of positional voting and preference aggregation.
Calculates credibility-weighted Borda counts, detects Condorcet winners via pairwise matrix,
and ranks multi-agent reasoning paths deterministically.
"""

from typing import List, Dict, Any, Tuple, Optional


class AgentBallot:
    def __init__(self, voter_id: str, ranking: List[str], weight: float = 1.0):
        self.voter_id = voter_id
        self.ranking = ranking  # Ordered highest preference to lowest preference
        self.weight = weight


class BordaPreferenceAggregator:
    def __init__(self, candidates: List[str]):
        self.candidates = candidates
        self.ballots: List[AgentBallot] = []

    def add_ballot(self, voter_id: str, ranking: List[str], weight: float = 1.0):
        # Validate ranking contains known candidates
        valid_ranking = [c for c in ranking if c in self.candidates]
        self.ballots.append(AgentBallot(voter_id, valid_ranking, weight))

    def compute_borda_scores(self) -> Dict[str, float]:
        n = len(self.candidates)
        scores: Dict[str, float] = {c: 0.0 for c in self.candidates}

        for b in self.ballots:
            m = len(b.ranking)
            for rank_idx, candidate in enumerate(b.ranking):
                # Standard Borda points: (m - 1 - rank_idx)
                points = (m - 1 - rank_idx) * b.weight
                scores[candidate] += points

        return scores

    def compute_pairwise_matrix(self) -> Dict[str, Dict[str, float]]:
        matrix: Dict[str, Dict[str, float]] = {c1: {c2: 0.0 for c2 in self.candidates} for c1 in self.candidates}

        for b in self.ballots:
            for i, c1 in enumerate(b.ranking):
                for j, c2 in enumerate(b.ranking):
                    if i < j:  # c1 preferred over c2
                        matrix[c1][c2] += b.weight

        return matrix

    def find_condorcet_winner(self) -> Optional[str]:
        matrix = self.compute_pairwise_matrix()
        for c1 in self.candidates:
            wins_all = True
            for c2 in self.candidates:
                if c1 == c2:
                    continue
                if matrix[c1][c2] <= matrix[c2][c1]:
                    wins_all = False
                    break
            if wins_all:
                return c1
        return None

    def rank(self) -> List[Tuple[str, float]]:
        scores = self.compute_borda_scores()
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
