<!-- source: fantomas-format — https://raw.githubusercontent.com/fsprojects/fantomas/main/.claude/commands/format.md -->
---
description: Format F# source code using the locally built Fantomas
allowed-tools: Bash(dotnet fsi:*), Bash(echo:*), Bash(dotnet build:*)
---

First build the project: `dotnet build src/Fantomas/Fantomas.fsproj`

Then run the format script. Pass a file path as argument:

```
dotnet fsi scripts/format.fsx [--editorconfig <content>] <file>
```

Or pipe inline source via stdin:

```
echo '<source>' | dotnet fsi scripts/format.fsx [--editorconfig <content>] [--signature]
```

$ARGUMENTS
