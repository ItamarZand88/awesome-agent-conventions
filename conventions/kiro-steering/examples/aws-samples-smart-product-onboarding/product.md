<!-- source: aws-samples-smart-product-onboarding — https://raw.githubusercontent.com/aws-samples/aws-smart-product-onboarding/main/.kiro/steering/product.md -->
# Smart Product Onboarding

An AWS accelerator that demonstrates AI-powered e-commerce product onboarding using generative AI for catalog management. The solution provides three core capabilities:

1. **Generate Product Data from Images** - Creates product titles and descriptions from images using Amazon Bedrock with Claude 3 Haiku
2. **Bottom-Up Product Categorization** - Automatically assigns products to hierarchical category trees using a two-step process with metaclasses and LLM categorization
3. **Extract Attributes** - Extracts category-specific product attributes using Claude 3.5 Sonnet

Built on AWS serverless architecture (Bedrock, Step Functions, Lambda) with a React demo website. Designed for retailers to efficiently manage large product catalogs with AI assistance while maintaining human oversight through manual auditing capabilities.

The accelerator handles ~100,000 products/month at approximately $2,200/month cost and supports multiple languages and category structures for global e-commerce businesses.
