<!-- source: openclaw-setup — https://raw.githubusercontent.com/ucsandman/OpenClaw-Setup/main/MEMORY.md -->
# MEMORY.md — Index

> This is a lightweight reference table. Detail lives in linked files.
> Load this every session (~1-2k tokens). Drill into detail files only when needed.

---

## ⚠️ Active Context (always load in main session)
These files contain critical ongoing context. Load at session start.
- `memory/people/user.md` — My human, always relevant
- `memory/projects/example-project.md` — Current active project

## 👤 People
| Name | Role | Last Contact | Detail | Triggers |
|------|------|-------------|--------|----------|
| [User Name] | Human/Boss | [Date] | [user.md](memory/people/user.md) | user, boss, human |
| [Agent Name] | AI Colleague | [Date] | [colleague.md](memory/people/colleague.md) | agent, colleague |
| [Contact 1] | Friend | [Date] | [contact1.md](memory/people/contact1.md) | contact1 |
| [Contact 2] | Client | [Date] | [contact2.md](memory/people/contact2.md) | contact2 |

## 📁 Projects
| Project | Status | Updated | Detail | Triggers |
|---------|--------|---------|--------|----------|
| Example Project | Active | [Date] | [example-project.md](memory/projects/example-project.md) | project, example |
| Side Project | Planning | [Date] | [side-project.md](memory/projects/side-project.md) | side |
| Learning Goal | Active | [Date] | [learning-goal.md](memory/projects/learning-goal.md) | learning |

## 📋 Recent Decisions (last 30 days)
| Date | Decision | Detail |
|------|----------|--------|
| [Date] | [Decision description] | [Link to detail] |
| [Date] | [Decision description] | [Link to detail] |

## 🔧 Active Preferences
- [Preference 1]: [value]
- [Preference 2]: [value]
- [Preference 3]: [value]

## 🧠 Drill-Down Rules
1. **Conversation mentions a person?** → Load their people/ file
2. **Working on a project?** → Load its projects/ file
3. **Making a decision?** → Check decisions/ for precedent
4. **Unsure about context?** → Use memory_search or vector memory
5. **Session start:** Always load Active Context files (max 2-3)
6. **Hard cap:** Max 5 drill-downs at session start

## 📂 Other Reference Files
| File | What |
|------|------|
| memory/accounts.md | Service accounts and platforms |
| memory/pending-tasks.md | Open tasks |
| docs/agent-architecture.md | Multi-agent architecture |
| docs/task-routing.md | Delegation rules |
| docs/morning-brief-template.md | Morning brief structure |

## 🗄️ Daily Logs
Raw daily logs live in `memory/YYYY-MM-DD.md`. These are append-only journals.
Only load when you need specific detail about what happened on a particular day.

---

*Last updated: [Date]*
*Update this index whenever you update a detail file. Same commit. No exceptions.*
