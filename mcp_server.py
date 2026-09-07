"""
MCP Server for Weighted Borda Count Preference Aggregator Skill
"""

import json
import sys
from client import BordaPreferenceAggregator

def handle_call(name: str, args: dict) -> dict:
    if name == "aggregate_votes":
        candidates = args.get("candidates", [])
        ballots = args.get("ballots", [])
        agg = BordaPreferenceAggregator(candidates)
        for b in ballots:
            agg.add_ballot(b.get("voter_id", "anon"), b.get("ranking", []), b.get("weight", 1.0))
        return {
            "ranking": agg.rank(),
            "borda_scores": agg.compute_borda_scores(),
            "condorcet_winner": agg.find_condorcet_winner()
        }
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
