# Personal AI Employee - Bronze Tier

A local-first autonomous AI employee that proactively manages personal and business affairs using Claude Code and Obsidian.

## Architecture Overview

This bronze tier implementation includes:

- **Brain**: Claude Code as the reasoning engine
- **Memory**: Obsidian vault as the knowledge base and dashboard
- **Senses**: Python watcher scripts for Gmail and file system monitoring
- **Hands**: MCP servers for external actions

## Quick Start

### Prerequisites

1. Install required software:
   - [Claude Code](https://claude.com/product/claude-code)
   - [Obsidian](https://obsidian.md/download)
   - Python 3.13+
   - Node.js 24+

2. Set up your Obsidian vault:
   ```bash
   # Create the vault directory
   mkdir -p AI_Employee_Vault/{Inbox,Needs_Action,Done,Pending_Approval,Approved,Rejected,Plans,Logs,Accounting,Invoices,Briefings}
   ```

### Configuration

1. Configure Claude Code MCP servers:
   ```bash
   # Copy the MCP config
   cp mcp_config.json ~/.config/claude-code/
   ```

2. Set up environment variables:
   ```bash
   # Add to your .env or system environment
   export VAULT_PATH="C:/Users/rehman/hackathon-0/bronze-tier/AI_Employee_Vault"
   export GMAIL_CREDENTIALS="C:/path/to/gmail_credentials.json"
   ```

### Running the System

1. Start the Gmail watcher:
   ```bash
   python gmail_watcher.py
   ```

2. Start the file system watcher:
   ```bash
   python filesystem_watcher.py
   ```

3. Open Obsidian and point it to your vault

4. Start Claude Code in the vault directory:
   ```bash
   claude .
   ```

## File Structure

```
AI_Employee_Vault/
├── Dashboard.md                 # Main dashboard and summary
├── Company_Handbook.md         # Rules and guidelines
├── Inbox/                      # New incoming items
├── Needs_Action/               # Items requiring AI processing
├── Done/                       # Completed items
├── Pending_Approval/           # Items awaiting human approval
├── Approved/                   # Approved items ready for action
├── Rejected/                   # Rejected items
├── Plans/                      # AI-generated action plans
├── Logs/                       # System logs and audit trails
├── Accounting/                 # Financial records and transactions
├── Invoices/                   # Generated invoices
└── Briefings/                  # Weekly summaries and reports
```

## How It Works

1. **Detection**: Watchers monitor Gmail and file system for new items
2. **Processing**: New items are moved to Needs_Action folder
3. **Reasoning**: Claude Code reads items and creates plans in Plans folder
4. **Approval**: Critical actions require approval in Pending_Approval
5. **Action**: Approved items are processed via MCP servers
6. **Completion**: Finished items are moved to Done folder

## Gmail Watcher

The Gmail watcher monitors for important unread emails and creates action files:

- Monitors `is:unread is:important` queries
- Creates markdown files with email metadata
- Suggests automated actions
- Logs all activity for audit trails

### Setup

1. Enable Gmail API in Google Cloud Console
2. Download credentials JSON file
3. Update `gmail_watcher.py` with your credentials path
4. Run the watcher

## File System Watcher

The file system watcher monitors a drop folder for new files:

- Watches specified directory for new files
- Creates action files with file metadata
- Supports automated processing based on file type
- Maintains audit logs

### Setup

1. Create a drop folder (e.g., `AI_Employee_Drop`)
2. Update `filesystem_watcher.py` with your watch path
3. Run the watcher
4. Drop files into the folder to trigger processing

## MCP Servers

Model Context Protocol servers provide external actions:

- **Filesystem**: Read/write files in the vault
- **Email**: Send and manage emails
- **Browser**: Web automation for payments and forms

### Configuration

Update `mcp_config.json` with your server paths and credentials.

## Agent Skills

All AI functionality is implemented as Agent Skills following the Claude Code Skills framework.

### Creating Skills

1. Create a new skill directory in `.claude/skills/`
2. Add a `SKILL.md` file with skill definition
3. Implement the skill logic
4. Test the skill functionality

### Available Skills

- **Gmail Monitoring**: Watch for important emails
- **File Processing**: Handle dropped files automatically
- **Dashboard Management**: Update dashboard with current status
- **Task Planning**: Create action plans for complex tasks

## Security & Privacy

### Data Protection

- All data stays local by default
- Credentials stored in environment variables
- Audit logs for all actions
- Human-in-the-loop for sensitive operations

### Access Control

- Local-only access for sensitive operations
- Cloud-only for non-sensitive monitoring
- No direct payment processing in cloud
- All approvals require human verification

## Troubleshooting

### Common Issues

1. **Gmail API not working**: Check credentials and API enablement
2. **Watchers not running**: Verify Python dependencies and paths
3. **Claude not reading files**: Check file permissions and vault path
4. **MCP servers not connecting**: Verify server processes and config

### Debug Mode

Enable debug logging by setting environment variable:
```bash
export DEBUG=True
```

## Next Steps (Silver Tier)

To upgrade to Silver Tier:

1. Add WhatsApp watcher using Playwright
2. Implement LinkedIn posting functionality
3. Create Claude reasoning loop with Plan.md files
4. Add MCP server for email sending
5. Implement human-in-the-loop approval workflow
6. Set up scheduling with cron or Task Scheduler

## License

This project is part of the Personal AI Employee Hackathon. All code is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For questions and support:
- Join the Wednesday Research Meeting (Zoom link in documentation)
- Check the Discord community
- Open an issue in the repository

---

**Built with Claude Code and Obsidian**
*Bronze Tier - Minimum Viable Personal AI Employee*