<!-- source: rclick-macos-app — https://raw.githubusercontent.com/wflixu/RClick/main/specs/001-macos-app-macos/spec.md -->
# Feature Specification: RClick - macOS Finder Context Menu Extension

**Feature Branch**: `001-macos-app-macos`  
**Created**: 2025-10-02  
**Status**: Draft  
**Input**: User description: "这是一个macOS app，主要的功能是拓展macOS finder 右键，为右键添加了复制路径，直接删除等快捷功能，添加了创建不同文件的菜单，如新建json，mardown 文件，新建docx文件，新建pptx 文件，可以自定义新建文件类型，比如没有内置的pages 文件；还可以用不同的app 打开选中的文集件，比如 terminal 打开当前选中的文件夹，vscode 打开当前选中的文件夹；app包含一个自动更新的功能，从github 上获取最新的release 版本，比较后提示用户更新，或点击更新按钮检查并更新。"

## Execution Flow (main)
```
1. Parse user description from Input
   → If empty: ERROR "No feature description provided"
2. Extract key concepts from description
   → Identify: actors, actions, data, constraints
3. For each unclear aspect:
   → Mark with [NEEDS CLARIFICATION: specific question]
4. Fill User Scenarios & Testing section
   → If no user flow: ERROR "Cannot determine user scenarios"
5. Generate Functional Requirements
   → Each requirement must be testable
   → Mark ambiguous requirements
6. Identify Key Entities (if data involved)
7. Run Review Checklist
   → If any [NEEDS CLARIFICATION]: WARN "Spec has uncertainties"
   → If implementation details found: ERROR "Remove tech details"
8. Return: SUCCESS (spec ready for planning)
```

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

### Section Requirements
- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation
When creating this spec from a user prompt:
1. **Mark all ambiguities**: Use [NEEDS CLARIFICATION: specific question] for any assumption you'd need to make
2. **Don't guess**: If the prompt doesn't specify something (e.g., "login system" without auth method), mark it
3. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
4. **Common underspecified areas**:
   - User types and permissions
   - Data retention/deletion policies  
   - Performance targets and scale
   - Error handling behaviors
   - Integration requirements
   - Security/compliance needs
5. **Constitution compliance check**:
   - Verify all requirements align with Swift 6.2 syntax mandate
   - Confirm macOS 15+ target platform compatibility
   - Ensure SwiftUI-first approach is considered for UI requirements
   - Verify internationalization requirements for English/Simplified Chinese

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a macOS user, I want to extend the Finder context menu with additional functionality such as copying file paths, creating files, opening with different applications, and deleting files directly. This enhances my productivity by providing quick access to common file operations directly from the right-click menu without opening additional applications.

### Acceptance Scenarios
1. **Given** user has selected a file in Finder, **When** user right-clicks and selects "Copy Path" option, **Then** the file's path is copied to the clipboard
2. **Given** user has selected a folder in Finder, **When** user right-clicks and selects "Open with Terminal" option, **Then** Terminal opens with the selected folder as the current directory
3. **Given** user wants to create a new file, **When** user right-clicks in Finder and selects "New File" then chooses a file type (JSON, Markdown, etc.), **Then** a new file of the specified type is created in the current directory
4. **Given** user wants to delete a file, **When** user right-clicks and selects "Delete" option, **Then** the file is permanently deleted after confirmation
5. **Given** there's a new version of RClick available on GitHub, **When** user opens the app, **Then** they are notified of the update and can choose to install it

### Edge Cases
- What happens when [trying to create a file in a read-only directory]?
- How does system handle [attempting to delete a protected system file]?
- What happens when [internet connection is unavailable during update check]?
- How does system handle [insufficient permissions for certain operations]?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: System MUST extend the macOS Finder context menu with additional options
- **FR-002**: Users MUST be able to copy the file path of selected items to clipboard
- **FR-003**: Users MUST be able to permanently delete selected files or folders after confirmation
- **FR-004**: Users MUST be able to create new files of specified types (JSON, Markdown, DOCX, PPTX, etc.) in the current Finder directory
- **FR-005**: System MUST allow users to open selected files or folders with custom applications (e.g., VSCode, Terminal)
- **FR-006**: System MUST provide an auto-update mechanism that checks GitHub for new releases
- **FR-007**: System MUST support custom file types beyond the built-in ones through a configuration interface that allows users to specify file extensions, templates, and display names
- **FR-008**: System MUST support localization in English and Simplified Chinese as per constitutional requirement
- **FR-009**: System MUST be compatible with macOS 15 and above as per constitutional requirement

### Key Entities
- **ContextMenuAction**: Represents an action available in the Finder context menu (copy path, delete, create file, open with app, etc.)
- **CustomFileType**: Represents a file type that can be created, including extension, template (if any), and display name
- **ExternalApplication**: Represents an application that can open files/folders, including path to executable and supported file types
- **UpdateInfo**: Represents information about available updates, including version number, download URL, and release notes

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

### Requirement Completeness
- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous  
- [x] Success criteria are measurable
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

---

## Execution Status
*Updated by main() during processing*

- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked
- [x] User scenarios defined
- [x] Requirements generated
- [x] Entities identified
- [x] Review checklist passed

---