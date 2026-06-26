<!-- source: wshobson-backtesting-frameworks — https://raw.githubusercontent.com/wshobson/agents/main/plugins/quantitative-trading/skills/backtesting-frameworks/SKILL.md -->
---
name: backtesting-frameworks
description: Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship bias, and transaction costs. Use when developing trading algorithms, validating strategies, or building backtesting infrastructure.
---

# Backtesting Frameworks

Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates.

## When to Use This Skill

- Developing trading strategy backtests
- Building backtesting infrastructure
- Validating strategy performance
- Avoiding common backtesting biases
- Implementing walk-forward analysis
- Comparing strategy alternatives

## Core Concepts

### 1. Backtesting Biases

| Bias             | Description               | Mitigation              |
| ---------------- | ------------------------- | ----------------------- |
| **Look-ahead**   | Using future information  | Point-in-time data      |
| **Survivorship** | Only testing on survivors | Use delisted securities |
| **Overfitting**  | Curve-fitting to history  | Out-of-sample testing   |
| **Selection**    | Cherry-picking strategies | Pre-registration        |
| **Transaction**  | Ignoring trading costs    | Realistic cost models   |

### 2. Proper Backtest Structure

```
Historical Data
      │
      ▼
┌─────────────────────────────────────────┐
│              Training Set               │
│  (Strategy Development & Optimization)  │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│             Validation Set              │
│  (Parameter Selection, No Peeking)      │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│               Test Set                  │
│  (Final Performance Evaluation)         │
└─────────────────────────────────────────┘
```

### 3. Walk-Forward Analysis

```
Window 1: [Train──────][Test]
Window 2:     [Train──────][Test]
Window 3:         [Train──────][Test]
Window 4:             [Train──────][Test]
                                     ─────▶ Time
```

## Detailed worked examples and patterns

Detailed sections (starting with `## Implementation Patterns`) live in `references/details.md`. Read that file when the navigation summary above is insufficient.

## Best Practices

### Do's

- **Use point-in-time data** - Avoid look-ahead bias
- **Include transaction costs** - Realistic estimates
- **Test out-of-sample** - Always reserve data
- **Use walk-forward** - Not just train/test
- **Monte Carlo analysis** - Understand uncertainty

### Don'ts

- **Don't overfit** - Limit parameters
- **Don't ignore survivorship** - Include delisted
- **Don't use adjusted data carelessly** - Understand adjustments
- **Don't optimize on full history** - Reserve test set
- **Don't ignore capacity** - Market impact matters
