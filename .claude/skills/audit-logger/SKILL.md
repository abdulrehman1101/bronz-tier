# Audit Logging Skill

## Purpose
Maintain comprehensive audit trails of all system activity and AI decisions.

## Inputs
- All file operations and AI actions
- Decision points and outcomes
- Approval workflows
- Error conditions and recovery

## Outputs
- Structured log files in Logs folder
- Activity summaries
- Audit reports
- Compliance documentation

## Dependencies
- Access to all vault folders
- File system monitoring
- Time tracking

## Security Considerations
- Read access to all folders
- Write access only to Logs folder
- No external data access
- Sensitive data handling

## Usage

### Basic Usage
```
claude --skill audit-logger
```

### With Custom Parameters
```
claude --skill audit-logger --log-level detailed --period daily
```

## Examples

### Log File Operation
```
claude --skill audit-logger --action file-created --path /path/to/file
```

### Generate Audit Report
```
claude --skill audit-logger --action generate-report --period weekly
```