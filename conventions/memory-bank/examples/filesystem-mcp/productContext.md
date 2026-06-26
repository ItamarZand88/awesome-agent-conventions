<!-- source: filesystem-mcp — https://raw.githubusercontent.com/SylphxAI/filesystem-mcp/main/memory-bank/productContext.md -->
<!-- Version: 4.5 | Last Updated: 2025-04-06 | Updated By: Roo -->

# Product Context: Filesystem MCP Server

## 1. Problem Solved

AI agents like Cline often need to interact with a user's project files to
perform tasks such as reading code, writing new code, modifying configurations,
or searching for specific information. Directly granting unrestricted filesystem
access poses significant security risks. Furthermore, requiring the user to
manually perform every filesystem action requested by the agent is inefficient
and hinders the agent's autonomy.

This Filesystem MCP server acts as a secure and controlled bridge, solving the
following problems:

- **Security:** It confines the agent's filesystem operations strictly within
  the boundaries of the project root directory (determined by the server's
  launch context), preventing accidental or malicious access to sensitive system
  files outside the project scope.
- **Efficiency:** It provides the agent with a dedicated set of tools
  (`list_files`, `read_content`, `write_content`, `move_items`, `copy_items`,
  etc.) to perform common filesystem tasks directly, reducing the need for
  constant user intervention for basic operations.
- **Control:** Operations are performed relative to the project root (determined
  by the server's current working directory at launch), ensuring predictability
  and consistency within that specific project context. **Note:** For
  multi-project support, the system launching the server must set the correct
  working directory for each project instance.
- **Standardization:** It uses the Model Context Protocol (MCP), providing a
  standardized way for the agent and the server to communicate about filesystem
  capabilities and operations.

## 2. How It Should Work

- The server runs as a background process, typically managed by the agent's host
  environment (e.g., Cline's VSCode extension).
- It listens for incoming MCP requests over a defined transport (initially
  stdio).
- Upon receiving a `call_tool` request for a filesystem operation:
  1. It validates the request parameters against the tool's schema.
  2. It resolves all provided relative paths against the `PROJECT_ROOT` (which
     is the server process's current working directory, `process.cwd()`).
  3. It performs security checks to ensure paths do not attempt to escape the
     `PROJECT_ROOT` (the server's `cwd`).
  4. It executes the corresponding Node.js filesystem function (`fs.readFile`,
     `fs.writeFile`, `fs.rename`, `glob`, etc.).
  5. It formats the result (or error) according to MCP specifications and sends
     it back to the agent.
- It responds to `list_tools` requests by providing a list of all available
  filesystem tools and their input schemas.

## 3. User Experience Goals

- **Seamless Integration:** The server should operate transparently in the
  background. The user primarily interacts with the agent, and the agent
  utilizes the server's tools as needed.
- **Security Assurance:** The user should feel confident that the agent's
  filesystem access is restricted to the intended project directory.
- **Reliability:** The tools should perform filesystem operations reliably and
  predictably. Errors should be reported clearly back to the agent (and
  potentially surfaced to the user by the agent if necessary).
- **Performance:** Filesystem operations should be reasonably fast, not
  introducing significant delays into the agent's workflow.
