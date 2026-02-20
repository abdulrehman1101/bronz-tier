# Dashboard Management Skill

## Purpose
Maintain and update the main dashboard with current system status and activity summary.

## Inputs
- Current state of all folders in the vault
- Recent activity logs
- Pending items across different categories

## Outputs
- Updated Dashboard.md with current status
- Executive summary of system health
- Quick actions and next steps

## Dependencies
- File system access to vault directories
- Logging system for activity tracking

## Security Considerations
- Read-only access to most folders
- Write access only to Dashboard.md
- No external API calls required

## Usage

### Basic Usage
```
claude --skill dashboard
```

### With Custom Path
```
claude --skill dashboard --vault-path /path/to/vault
```

## Examples

### Update Dashboard
```
claude --skill dashboard --action update
```

### Generate Report
```
claude --skill dashboard --action report --period daily
```