# Gmail Monitoring Skill

## Purpose
Monitor Gmail for important messages and create action items in the Obsidian vault.

## Inputs
- Gmail API credentials
- Vault path for storing action files
- Search criteria for important emails

## Outputs
- Markdown files in Needs_Action folder
- Email metadata and suggested actions
- Activity logs

## Dependencies
- Gmail API credentials
- Google OAuth setup
- Network connectivity

## Security Considerations
- Requires OAuth tokens stored securely
- Only accesses authorized Gmail account
- Logs all email processing activity

## Usage

### Basic Usage
```
claude --skill gmail-monitor
```

### With Custom Configuration
```
claude --skill gmail-monitor --credentials /path/to/credentials.json --vault /path/to/vault
```

## Examples

### Check for New Emails
```
claude --skill gmail-monitor --check-now
```

### Configure Email Filters
```
claude --skill gmail-monitor --add-filter "from:client@example.com is:unread"
```