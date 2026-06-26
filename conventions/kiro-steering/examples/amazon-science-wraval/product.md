<!-- source: amazon-science-wraval — https://raw.githubusercontent.com/amazon-science/wraval/main/.kiro/steering/product.md -->
# Product Overview

## WRAVAL – WRiting Assist eVALuation

WRAVAL is an evaluation framework for assessing Large Language Models (LLMs) and Small Language Models (SLMs) on writing assistant tasks. It focuses on non-reasoning tasks like tone transformation, summarization, and text improvement.

### Purpose

The framework addresses a gap in LM evaluation by focusing on practical writing assistant use cases rather than general reasoning tasks. It demonstrates that SLMs (under 10B parameters) can perform competitively on specific writing tasks despite scoring lower on general intelligence benchmarks.

### Core Capabilities

1. **Data Generation**: Synthetic dataset creation for various writing tasks using LLMs
2. **Inference**: Running writing assistant tasks on both Bedrock-hosted and self-hosted models
3. **Evaluation**: LLM-as-a-judge and human evaluation workflows
4. **Deployment**: SageMaker endpoint deployment for custom models

### Supported Writing Tasks (Tones)

- **witty**: Transform factual sentences to witty versions
- **professional**: Convert casual text to professional tone
- **casual**: Make formal text more casual
- **elaborate**: Expand simple sentences with detail
- **shorten**: Condense wordy text
- **improve**: Enhance poorly written sentences
- **keypoints**: Extract key points from paragraphs
- **proofread**: Correct errors in text
- **emojify**: Add emojis to plain text
- **summarize**: Create paragraph summaries

### Target Users

- ML practitioners evaluating SLMs for edge/private computing
- Researchers benchmarking models on specific writing tasks
- Teams implementing writing assistant features

### Key Innovation

The framework enables evaluation of models on tasks they excel at, rather than forcing comparison on general reasoning benchmarks where SLMs underperform.
