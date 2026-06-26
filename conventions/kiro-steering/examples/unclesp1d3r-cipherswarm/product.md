<!-- source: unclesp1d3r-cipherswarm — https://raw.githubusercontent.com/unclesp1d3r/CipherSwarm/main/.kiro/steering/product.md -->
---
inclusion: always
---

# CipherSwarm Product Overview

CipherSwarm is a distributed hash cracking system built on Ruby on Rails, designed for efficiency and scalability. It's inspired by Hashtopolis and provides a web-based interface for managing and distributing hash-cracking tasks across multiple nodes.

## Core Concepts

The system is built around four main entities:

- **Campaigns**: Comprehensive units of work focused on a single hash list with priority-based execution
- **Attacks**: Defined units of hashcat work with specific attack types, word lists, and rules
- **Tasks**: Smallest work units distributed to individual agents for parallel processing
- **Agents**: Distributed nodes that execute cracking tasks using hashcat

## Key Features

- Distributed hash-cracking with web-based management interface
- Priority-based campaign execution with enum values (deferred, routine, priority, urgent, immediate, flash, flash_override)
- Integration with hashcat for versatile hash cracking capabilities
- Real-time monitoring and comprehensive result reporting
- Support for multiple attack modes: dictionary, mask, hybrid_dictionary, hybrid_mask

## Target Environment

- Medium to large-scale cracking infrastructure
- High-speed network connections (LAN environment)
- Trusted client machines under direct user control
- Organizational/project team usage (not public internet)
- Exclusively supports Hashcat as the cracking tool
