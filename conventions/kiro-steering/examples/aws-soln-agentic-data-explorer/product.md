<!-- source: aws-soln-agentic-data-explorer — https://raw.githubusercontent.com/aws-solutions-library-samples/guidance-for-agentic-data-exploration-on-aws/main/.kiro/steering/product.md -->
# AI Data Explorer Product Overview

## Product Description
AI Data Explorer is a multi-agent Python application with a web UI that provides intelligent data analysis and exploration powered by AWS AI services. The system features a supervisor agent that routes queries to specialized agents and runs as containerized services in AWS Fargate.

## Core Architecture
- **Multi-agent system** with supervisor routing to specialized agents
- **Containerized deployment** using AWS Fargate with CloudFront HTTPS termination
- **Web UI** with Amazon Q-style chat interface and streaming responses
- **Optional Neptune graph database** for advanced graph analytics

## Available Agents
- **Supervisor Agent**: Classifies requests and routes to specialized agents
- **Product Analyst**: Product analysis using knowledge base
- **Weather Agent**: Weather forecasts and meteorological information
- **Schema Agent**: Database schema analysis and graph model conversion
- **Data Visualizer Agent**: Creates charts, tables, and word clouds
- **Image Assistant**: Image analysis and generation using AI models
- **Help Assistant**: Application guidance using help knowledge base
- **General Agent**: Handles all other topics outside specialized domains

## Key Features
- Streaming chat responses with conversation history
- File upload support (SQL, images, text files)
- Prompt suggestions and debug mode
- Mobile-responsive design
- Comprehensive tracing and observability
- LLM-as-a-judge evaluation framework