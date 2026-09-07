# GenPark Weighted Borda Count Preference Aggregator Skill

Weighted positional Borda voting and Condorcet preference aggregation engine for multi-agent swarms.

Check out [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    A[Agent Proposal Ballots] --> B[Credibility Weight Scaler]
    B --> C[Positional Borda Points]
    B --> D[Pairwise Head-to-Head Matrix]
    C --> E[Final Ranked Order]
    D --> F{Condorcet Winner?}
    F -->|Exists| G[Dominant Equilibrium Proposal]
    F -->|Cycle| H[Borda Tie-Breaker Applied]
```

## Features
- Weighted Borda count calculation with dynamic agent reputation multipliers.
- Pairwise tournament matrix and Condorcet winner detection.
- Pure Python standard library implementation.
