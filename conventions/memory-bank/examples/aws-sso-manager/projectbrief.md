<!-- source: aws-sso-manager — https://raw.githubusercontent.com/cfircoo/aws-sso-manager/main/memory-bank/projectbrief.md -->
# Project Brief: AWS SSO Manager

## Project Name
AWS SSO Manager

## Version
2.0.0

## Mission Statement
A modern desktop application that simplifies AWS Single Sign-On (SSO) session management and role switching across multiple AWS accounts, providing a seamless and intuitive user experience for developers and cloud engineers.

## Core Requirements

### Functional Requirements
1. **SSO Authentication**
   - Easy AWS SSO login and session management
   - Automatic session refresh capabilities
   - Session expiration tracking with visual indicators

2. **Account & Role Management**
   - Switch between multiple AWS accounts and roles
   - Fast role switching with favorites functionality
   - Quick Access feature for frequently used roles
   - Search capabilities for quick account and role access

3. **Integration Features**
   - ECR (Elastic Container Registry) integration
   - CodeArtifact integration
   - Direct AWS Console access for any role with one click
   - Kubernetes/EKS cluster management and kubectl configuration

4. **User Interface**
   - Modern glassmorphism design system with enhanced animations
   - Dark mode support with improved theming
   - Visual account counter to track available AWS accounts
   - Loading indicators for better user experience
   - Manual refresh button for account list updates
   - Buy Me a Coffee integration for donation support
   - Recently used regions tracking for better UX

### Non-Functional Requirements
1. **Security**
   - Secure credential storage using system keychain/credential manager
   - No plain text storage of AWS credentials
   - Secure session token management

2. **Performance**
   - Fast application startup
   - Efficient role switching
   - Responsive UI with proper loading states

3. **Platform Support**
   - macOS 10.15 or later
   - Windows 10/11
   - Cross-platform consistency

## Target Audience
- AWS developers and engineers
- DevOps professionals
- Cloud architects
- Anyone managing multiple AWS accounts and roles

## Project Scope
- Desktop application (not web-based)
- AWS SSO integration (not traditional IAM)
- Read and manage existing AWS configurations
- No direct AWS resource manipulation (purely authentication/session management)

## Success Metrics
- Reduced time to switch between AWS roles
- Improved user satisfaction with AWS credential management
- Secure handling of all authentication tokens
- Stable application with minimal crashes

## Current Branch Context
Currently on "sso-manager-v2" branch - major version 2.0.0 with modern UI redesign and Kubernetes integration

## License
MIT License with Commons Clause - free to use and modify but cannot be sold commercially without permission
