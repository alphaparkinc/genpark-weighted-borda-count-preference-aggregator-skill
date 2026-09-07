"""
Demonstration of Weighted Borda Count Preference Aggregator Skill
"""

from client import BordaPreferenceAggregator

def main():
    print("=== Aggregating Multi-Agent Proposal Preferences ===")
    candidates = ["plan_alpha", "plan_beta", "plan_gamma", "plan_delta"]
    aggregator = BordaPreferenceAggregator(candidates)

    # Lead Researcher Agent (high credibility 2.5)
    aggregator.add_ballot("researcher_01", ["plan_beta", "plan_alpha", "plan_gamma", "plan_delta"], weight=2.5)
    # Security Auditor Agent (weight 2.0)
    aggregator.add_ballot("auditor_01", ["plan_alpha", "plan_beta", "plan_delta", "plan_gamma"], weight=2.0)
    # Execution Worker Agent (weight 1.0)
    aggregator.add_ballot("worker_01", ["plan_beta", "plan_gamma", "plan_alpha", "plan_delta"], weight=1.0)

    scores = aggregator.compute_borda_scores()
    print("Weighted Borda Scores:", scores)

    ranking = aggregator.rank()
    print("Ranked Proposals:")
    for rank_pos, (candidate, score) in enumerate(ranking, 1):
        print(f"  {rank_pos}. {candidate} (Score: {score:.2f})")

    condorcet = aggregator.find_condorcet_winner()
    print("Condorcet Winner:", condorcet)
    assert condorcet is not None
    print("Borda Count Preference Aggregator Verification PASS!")

if __name__ == "__main__":
    main()
