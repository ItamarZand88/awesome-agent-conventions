<!-- source: qwen-zkeacms — https://raw.githubusercontent.com/SeriaWei/ZKEACMS/master/QWEN.md -->
# ZKEACMS - Project Context for Qwen Code

## Project Overview

ZKEACMS is a visual design, **WYSIWYG** Content Management System built with .NET 9. It features a modern responsive design that automatically adapts to different screen sizes and devices. The system allows users to create pages with a drag-and-drop interface, add content through widgets, and customize themes using LESS CSS.

## Technology Stack

- **Backend**: .NET 9, ASP.NET Core, Entity Framework Core
- **Frontend**: Bootstrap 3, JavaScript, jQuery
- **Testing**: MSTest, Moq

## Project Structure

The solution contains multiple projects organized in a modular architecture:

### Main Projects
- `~/src/EasyFrameWork` - Custom framework components
- `~/src/ZKEACMS` - Core CMS functionality
- `~/src/Plugins` - CMS plugins
- `~/src/ZKEACMS.WebHost` - Main web application host
- `~/test` - Test projects

## Testing

Unit and integration tests are implemented using MSTest with Moq for mocking. UI testing is done with Selenium.

Run tests with:
```bash
dotnet test
```