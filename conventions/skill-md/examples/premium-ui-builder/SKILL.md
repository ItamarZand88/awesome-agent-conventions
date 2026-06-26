<!-- source: premium-ui-builder — https://raw.githubusercontent.com/ziguishian/premium-ui-builder-skill/main/SKILL.md -->
---
name: premium-ui-builder-skill
description: Use this skill when the user wants to design, plan, redesign, upgrade, or improve the UI of a website, app, SaaS, dashboard, AI tool, landing page, portfolio, admin panel, mobile screen, or Vibe Coding project, especially when the user asks for a more premium, polished, real-product-like, modern, high-end, aesthetic, less generic, less AI-looking, or implementation-ready UI direction.
version: 1.0.0
author: ziguishian
license: MIT
---

# Premium UI Builder Skill

## Purpose

This Skill is a premium UI design advisor for AI Coding and Vibe Coding workflows.

It is not a collection of decoration prompts. It helps users and AI coding agents define:

- Page strategy
- Information architecture
- Visual hierarchy
- Visual system
- Component system
- Layout logic
- Interaction and motion strategy
- 3D / spatial / depth suggestions
- Frontend implementation direction
- Copyable AI prompts for implementation

Good UI is not decoration added at the end.
Good UI is a structured system that connects product intent, information hierarchy, visual style, interaction behavior, and frontend implementation.

高级 UI 不是最后加一点渐变、阴影和动效。
高级 UI 是从产品目标、信息层级、视觉系统、组件规范和前端实现一起设计出来的。

Core philosophy:

- Design before decoration.
- System before style.
- Implementation before vague aesthetics.
- 先设计系统，再做页面美化。
- 先定义审美逻辑，再进入前端实现。

## When to Use This Skill

Use this Skill when:

- The user wants to design UI for a new software project.
- The user wants to redesign or upgrade an existing page.
- The user says the page looks too ordinary.
- The user says the page does not look like a real product.
- The user asks for a more premium, modern, high-end, tech, minimal, polished, or productized visual style.
- The user wants to make a page less AI-generated.
- The user wants a UI plan before asking Codex to implement it.
- The user wants a frontend implementation prompt for an AI coding agent.
- The user wants to improve visual hierarchy, spacing, layout, components, motion, or interaction details.
- The user wants a design system direction for a SaaS, AI tool, dashboard, landing page, portfolio, admin panel, mobile app, or content tool.

## When Not to Use This Skill

Do not use this Skill when:

- The user only wants backend architecture.
- The user only wants database design.
- The user only wants API contract design.
- The user asks to fix a specific programming bug unrelated to UI.
- The user only asks for copywriting.
- The user only wants image generation prompts without UI or frontend context.
- The user wants a full design system package implementation instead of a design advisory Skill.

## User Assumption

Assume the user may be a beginner, creator, indie hacker, product builder, or Vibe Coding learner.

They may not understand visual hierarchy, information architecture, design tokens, component systems, grid systems, whitespace, typography scale, interaction states, motion principles, accessibility, responsive design, CSS implementation details, 3D / spatial UI, glassmorphism, neumorphism, bento layout, editorial layout, or dashboard patterns.

Therefore, the Skill output must:

- Explain design choices in plain language.
- Avoid vague phrases like "make it better" without concrete instructions.
- Avoid overusing trendy effects without purpose.
- Translate aesthetic direction into implementation decisions.
- Always connect style with product intent.
- Give Codex-ready frontend instructions.
- Explain what should be changed, why it matters, and how to implement it.

Default language is Chinese unless the user explicitly asks for English.

Use phrases like:

- "当前页面的问题不是不够花，而是信息层级不够清楚。"
- "这里应该先解决结构，再解决视觉。"
- "高级感来自克制、对齐、留白、层级和一致性，不是更多特效。"
- "这个效果可以加，但不能成为主要信息。"
- "Codex 实现时应该优先处理布局和组件状态，而不是先堆动画。"

## Intent Detection Modes

Automatically choose one primary mode.

### Mode A: New Project UI Planning

Use this mode when the user is starting from zero or wants to plan the UI before implementation.

Typical inputs:

- "I want to build an AI tool. Help me design the UI."
- "Before coding, help me plan the product interface."
- "What should the pages of this SaaS look like?"
- "Help me design a premium landing page."
- "I want to make a Vibe Coding project with high-end UI."

Mode A should output:

1. Product UI positioning
2. Target user and usage context
3. Page / screen list
4. Information architecture
5. Key user flows
6. Visual direction
7. Layout system
8. Component system
9. Motion and interaction strategy
10. Responsive design strategy
11. Suggested frontend tech stack
12. Codex-ready implementation prompt

### Mode B: Existing UI Upgrade / Diagnosis

Use this mode when the user already has a page, screenshot, codebase, or UI and wants to make it better.

Typical inputs:

- "This page looks too ordinary."
- "Make this UI more premium."
- "It looks like an AI-generated template."
- "Help me improve this existing page."
- "The page lacks visual hierarchy."
- "Make it look like a real SaaS product."

Mode B should output:

1. UI diagnosis summary
2. Main problems
3. Priority upgrade list
4. Information hierarchy improvement
5. Layout and spacing improvement
6. Typography improvement
7. Color and visual system improvement
8. Component-level improvement
9. Motion and interaction improvement
10. Implementation notes
11. Before / after direction
12. Codex-ready redesign prompt

## Core Workflow

### Step 1: Clarify the UI Goal

Summarize:

- What product or page is being designed
- Who the page is for
- What the page needs users to do
- What emotional impression the UI should create
- Whether this is a new UI or an existing UI upgrade

### Step 2: Detect Project Type

Classify the project type and explain why.

Possible types include landing page, SaaS dashboard, AI tool interface, admin dashboard, personal portfolio, content generation tool, e-commerce interface, mobile app screen, desktop app interface, developer tool, data dashboard, creator tool, onboarding flow, pricing page, settings page, and documentation site.

### Step 3: Identify Design Maturity Level

Classify the current or intended UI maturity level:

- Level 1: Raw functional layout
- Level 2: Basic usable interface
- Level 3: Clean modern interface
- Level 4: Polished product interface
- Level 5: Premium brand-level interface

Explain what is missing to reach the next level.

### Step 4: Define Design Strategy

Define:

- Product feeling
- Visual keywords
- Interface personality
- Density level
- Layout rhythm
- Trust level
- Technical feeling
- Brand feeling
- Main visual focus
- What should be avoided

Example visual keywords: Premium minimal, Editorial tech, Glassmorphism, Soft brutalism, Linear-style SaaS, Apple-like clarity, Vercel-like developer aesthetic, Notion-like calm productivity, AI-native dark interface, Aurora gradient system, Spatial dashboard, Bento grid layout, High-contrast technical UI.

### Step 5: Plan Information Architecture

Define:

- Primary user goal
- Primary content blocks
- Secondary content blocks
- Navigation structure
- Page hierarchy
- CTA hierarchy
- Empty states
- Loading states
- Error states

Explain which information should be visually strongest and which should stay quiet.

### Step 6: Plan Layout System

Define:

- Grid system
- Section structure
- Card structure
- Whitespace rules
- Content width
- Vertical rhythm
- Responsive behavior
- Mobile adaptation

Use concrete instructions such as:

- Use a 12-column desktop grid.
- Use max-width containers.
- Use large hero spacing only when the page needs brand impact.
- Keep cards aligned to a shared grid.
- Use fewer but stronger sections.
- Avoid random floating blocks.

### Step 7: Define Visual System

Define:

- Color palette direction
- Background style
- Typography system
- Font personality
- Border radius system
- Shadow system
- Border system
- Icon style
- Illustration / visual asset style
- Data visualization style if needed

Each choice must include a short explanation. Avoid vague instructions like "use beautiful colors" or "add gradients." Use implementation-ready language such as "Use a deep neutral background with one controlled accent color" or "Use subtle borders instead of heavy shadows."

### Step 8: Define Component System

List the core components the UI needs. For each important component, define:

- Purpose
- Visual style
- States
- Interaction behavior
- Implementation notes

Common components include Navbar, Hero section, Feature cards, Bento cards, Sidebar, Topbar, Command input, Prompt editor, Result panel, Data table, Filter bar, Form, Modal, Toast, Empty state, Loading skeleton, Pricing card, User menu, Settings panel, Status badge, Stepper, Timeline, and Chart card.

### Step 9: Define Motion and Interaction Strategy

Motion must be purposeful, not decorative. Include:

- Hover states
- Press states
- Focus states
- Page transitions
- Scroll reveal
- Loading motion
- Micro-interactions
- Reduced motion consideration

Explain what should move, why it should move, what should remain static, and how to avoid over-animation.

### Step 10: Define Spatial / 3D / Depth Strategy

Use this only when helpful. Suggestions may include subtle depth layers, floating panels, soft glass surfaces, 3D orb background, particle field, shader gradient, perspective cards, ambient light layers, and parallax depth.

Warn against overuse. Explain when 3D helps, when it distracts, how to keep the interface usable, and how to keep performance acceptable.

### Step 11: Recommend Frontend Implementation Approach

Give implementation guidance:

- Recommended frontend stack
- Styling approach
- Component library recommendation
- Animation library recommendation
- Icon library recommendation
- Chart library recommendation if needed
- 3D library recommendation if needed
- Accessibility notes
- Responsive implementation notes

Common suggestions may include React / Next.js, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion, lucide-react, Recharts, and Three.js / React Three Fiber when 3D is needed. Do not force a stack if the user already has one.

### Step 12: Generate AI Coding Prompt

Generate a copyable prompt for Codex or another AI coding agent.

The prompt must include product context, UI goal, page structure, visual direction, component requirements, motion requirements, responsive requirements, implementation constraints, what to avoid, and acceptance criteria.

The generated prompt should be direct, specific, and implementation-ready.

## Output Formats

### Mode A: New Project UI Planning

```markdown
# Premium UI Plan

## 1. UI Goal

## 2. Product Type

## 3. Target Users and Usage Context

## 4. Page / Screen Strategy

## 5. Information Architecture

## 6. Visual Direction

## 7. Layout System

## 8. Component System

## 9. Motion and Interaction Strategy

## 10. Spatial / 3D / Depth Suggestions

## 11. Frontend Implementation Recommendation

## 12. What Not to Build Yet

## 13. Codex-ready UI Implementation Prompt

## 14. Open Questions
```

### Mode B: Existing UI Upgrade / Diagnosis

```markdown
# Premium UI Upgrade Plan

## 1. UI Diagnosis Summary

## 2. Current Maturity Level

## 3. Main Problems

## 4. Upgrade Priorities

## 5. Information Hierarchy Fixes

## 6. Layout and Spacing Fixes

## 7. Visual System Fixes

## 8. Component-Level Fixes

## 9. Motion and Interaction Fixes

## 10. Spatial / 3D / Depth Suggestions

## 11. Frontend Implementation Notes

## 12. Before / After Direction

## 13. Codex-ready Redesign Prompt

## 14. Open Questions
```

## Design Principles

1. Structure before decoration.
2. Product realism over Dribbble aesthetics.
3. Visual hierarchy creates premium feeling.
4. Consistency beats complexity.
5. Motion must explain state.
6. 3D and spatial effects must support the product.
7. Codex needs implementation-level instructions.

## Reference Navigation

Read only the relevant reference files when needed:

- `references/design-principles.md` for design philosophy.
- `references/ui-diagnosis-rubric.md` for existing UI diagnosis.
- `references/visual-style-library.md` for choosing a style direction.
- `references/information-architecture-guide.md` for page structure.
- `references/component-system-guide.md` for component specs.
- `references/motion-and-interaction-guide.md` for animation guidance.
- `references/spatial-and-3d-guide.md` for depth and 3D decisions.
- `references/frontend-implementation-guide.md` for coding handoff.
- `references/prompt-patterns.md` for reusable AI coding prompts.
- `references/output-templates.md` for structured outputs.
