<!-- source: turboquantdc — https://raw.githubusercontent.com/dhawalc/turboQuantDC/master/MEMORY.md -->
# MEMORY.md — TurboQuantDC

## Key Learnings
_(accumulated during implementation)_

## Gotchas
- Per-vector reconstruction error is significant (23-44%). This is EXPECTED. TurboQuant preserves inner products, not individual vectors.
- The rotation matrix must be orthogonal (QR decomposition), not just random. Non-orthogonal rotation breaks the distribution assumptions.
- Lloyd-Max codebooks are precomputed for the target distribution, not learned from data. This is what makes TurboQuant "online" / data-oblivious.
- QJL projection dimension m should equal head dimension d for best results.

## Reference Implementation Notes
_(analysis of tonbistudio/turboquant-pytorch goes here)_
