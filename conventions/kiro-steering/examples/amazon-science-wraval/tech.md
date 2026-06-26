<!-- source: amazon-science-wraval — https://raw.githubusercontent.com/amazon-science/wraval/main/.kiro/steering/tech.md -->
# Technology Stack

## Build System & Package Management

- **Package Manager**: `uv` (modern Python package manager)
- **Build System**: setuptools with pyproject.toml
- **Python Version**: >=3.9

## Core Dependencies

### ML & AI Frameworks
- **transformers** (4.48.1): HuggingFace transformers for model loading
- **torch** (2.6.0): PyTorch for model inference
- **accelerate**: Distributed training and inference
- **bitsandbytes**: Quantization support (GPU optional dependency)

### AWS Integration
- **boto3**: AWS SDK for Python
- **sagemaker** (2.236.0): SageMaker model deployment
- **bedrock-runtime**: Bedrock model inference

### Data & Utilities
- **pandas** (2.2.3): Data manipulation
- **datasets** (3.2.0): HuggingFace datasets
- **dynaconf** (3.2.7): Configuration management
- **typer**: CLI framework
- **plotly** (5.24.1): Visualization
- **beautifulsoup4**: HTML parsing

## Configuration Management

Configuration is managed via `dynaconf` with environment-based settings in `config/settings.toml`:
- Model configurations (Bedrock, SageMaker, Ollama endpoints)
- AWS region and account settings
- S3 bucket paths for data and models
- Endpoint types and model mappings

## Common Commands

### Installation
```bash
# Standard installation
uv pip install .

# With GPU support (requires CUDA)
uv pip install ".[gpu]"
```

### CLI Commands
```bash
# Generate evaluation data
wraval generate --model haiku-3 --type witty

# Run inference on generated data
wraval inference --model nova-lite --type all

# Evaluate with LLM-as-a-judge
wraval llm_judge --model haiku-3 --type professional

# Deploy model to SageMaker
wraval deploy-model --model phi-3-5-4B

# Show examples from dataset
wraval show-examples --model haiku-3 --type witty --n-examples 10

# Upload for human evaluation
wraval human-judge-upload --type all --n-samples 100

# View results
wraval show-results --type all
```

### Common Options
- `--model, -m`: Model identifier from settings.toml
- `--type, -t`: Tone type (witty, professional, casual, etc. or 'all')
- `--upload-s3`: Upload results to S3
- `--custom-prompts`: Use custom prompt templates
- `--local-tokenizer-path`: Path to local tokenizer

## Project Structure

Entry point: `src/wraval/main.py` (CLI using Typer)

Key modules:
- `actions/`: Core functionality (generate, inference, judge, deploy)
- `custom_prompts/`: Prompt templates for different tones
- `model_artifacts/`: SageMaker deployment artifacts
- `config/settings.toml`: Model and AWS configuration

## Data Storage

- **Local**: `./data/` directory with timestamped CSV files
- **S3**: Configurable bucket paths for datasets and human evaluation
- **Format**: CSV files with columns for input, output, model, tone, timestamps

## Endpoint Types

1. **bedrock**: AWS Bedrock hosted models (Claude, Nova)
2. **sagemaker**: Self-hosted models on SageMaker endpoints
3. **ollama**: Local Ollama endpoints (for development)

## Development Notes

- AWS credentials required for Bedrock/SageMaker operations
- GPU support needed for model deployment (`bitsandbytes` dependency)
- Configuration uses string formatting for AWS account/region injection
- All CLI commands support `--help` for detailed usage
