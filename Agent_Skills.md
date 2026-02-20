# Agent Skills for Personal AI Employee

All AI functionality in the bronze tier is implemented as Agent Skills following the Claude Code Skills framework.

## Skill Structure

Each skill follows this structure:

```
.skills/
├── skill-name/
│   ├── SKILL.md              # Skill definition and metadata
│   ├── skill.py              # Main skill implementation
│   ├── requirements.txt      # Dependencies (if any)
│   └── README.md             # Documentation
```

## Available Skills

### 1. Dashboard Management

**Purpose**: Maintain and update the main dashboard with current system status.

**Location**: `.claude/skills/dashboard/`

**Key Functions**:
- Update executive summary
- Track pending items across folders
- Log recent activity
- Monitor system health

### 2. Gmail Monitoring

**Purpose**: Monitor Gmail for important messages and create action items.

**Location**: `.claude/skills/gmail-monitor/`

**Key Functions**:
- Check for unread important emails
- Create markdown action files
- Suggest response actions
- Log email processing

### 3. File Processing

**Purpose**: Handle files dropped in the monitoring folder.

**Location**: `.claude/skills/file-processor/`

**Key Functions**:
- Detect new files in drop folder
- Create action items with file metadata
- Suggest processing actions based on file type
- Log file processing

### 4. Task Planning

**Purpose**: Create comprehensive action plans for complex tasks.

**Location**: `.claude/skills/task-planner/`

**Key Functions**:
- Analyze needs from Needs_Action folder
- Create step-by-step plans in Plans folder
- Include approval requirements
- Set priority levels

### 5. Audit Logging

**Purpose**: Maintain comprehensive audit trails of all system activity.

**Location**: `.claude/skills/audit-logger/`

**Key Functions**:
- Log all file operations
- Track AI decisions and actions
- Record approval workflows
- Generate activity reports

## Skill Development Guidelines

### 1. Skill Definition

Each skill must have a `SKILL.md` file with:

```markdown
# Skill Name

## Purpose
Brief description of what the skill does

## Inputs
What the skill needs to function

## Outputs
What the skill produces

## Dependencies
Other skills or systems required

## Security Considerations
Any security requirements or constraints
```

### 2. Implementation Standards

- Use clear, descriptive function names
- Include comprehensive error handling
- Log all significant actions
- Follow the local-first principle
- Respect the human-in-the-loop requirements

### 3. Testing Requirements

Each skill should include:

- Unit tests for core functions
- Integration tests with other skills
- Security tests for sensitive operations
- Performance tests for resource usage

### 4. Documentation

Each skill must have:

- Clear usage examples
- Setup and configuration instructions
- Troubleshooting guide
- Security best practices

## Skill Communication

Skills communicate through the Obsidian vault file system:

1. **Input**: Read from specific folders (Needs_Action, Inbox, etc.)
2. **Processing**: Create intermediate files in Plans folder
3. **Output**: Write results to appropriate folders (Done, Approved, etc.)
4. **Logging**: Record all actions in Logs folder

## Security Framework

### Permission Levels

- **Read-Only**: Dashboard, Company_Handbook, Logs
- **Create**: Plans, Audit logs
- **Modify**: Needs_Action, Pending_Approval
- **Execute**: Approved actions via MCP

### Sensitive Operations

Skills that handle sensitive data must:

1. Require explicit approval for execution
2. Log all actions with full context
3. Never store credentials in plain text
4. Use environment variables for secrets
5. Implement proper error handling and recovery

## Integration Patterns

### 1. Sequential Processing

```
Needs_Action/
    ↓
Task Planning Skill
    ↓
Plans/
    ↓
Dashboard Update Skill
    ↓
Dashboard.md updated
```

### 2. Parallel Processing

```
Inbox/
    ├── Gmail Monitoring Skill
    └── File Processing Skill
        ↓
    └── Needs_Action/
```

### 3. Human-in-the-Loop

```
Needs_Action/
    ↓
Task Planning Skill
    ↓
Plans/
    ↓
Audit Logging Skill
    ↓
Pending_Approval/
    ↓
Human Review
    ↓
Approved/
    ↓
MCP Action Skill
    ↓
Done/
```

## Monitoring and Health

Each skill includes built-in monitoring:

- **Health Checks**: Verify skill can execute properly
- **Performance Metrics**: Track execution time and resource usage
- **Error Reporting**: Log and report failures
- **Dependency Checks**: Verify required services are available

## Future Skill Development

### Bronze Tier Extensions

1. **Email Response Skill**: Auto-generate email replies
2. **Calendar Management**: Handle scheduling and reminders
3. **Contact Management**: Organize and update contact information
4. **Task Prioritization**: Intelligent task sorting and prioritization

### Silver Tier Skills

1. **Social Media Management**: LinkedIn posting and monitoring
2. **WhatsApp Integration**: Handle WhatsApp messages
3. **Advanced Planning**: Complex multi-step workflows
4. **Analytics**: Generate insights from system data

### Gold Tier Skills

1. **Business Intelligence**: Automated business analysis
2. **Financial Management**: Expense tracking and budgeting
3. **Customer Relationship**: Advanced CRM functionality
4. **Project Management**: Full project lifecycle management

## Best Practices

### 1. Skill Design

- Keep skills focused and single-purpose
- Make skills composable and reusable
- Design for failure and graceful degradation
- Include comprehensive logging and monitoring

### 2. Security

- Never trust input data
- Validate all external inputs
- Use principle of least privilege
- Implement proper error handling
- Log all security-relevant events

### 3. Performance

- Optimize for local execution
- Minimize external API calls
- Cache frequently accessed data
- Use efficient data structures
- Implement proper resource cleanup

### 4. Maintainability

- Use clear, consistent naming conventions
- Include comprehensive documentation
- Write modular, testable code
- Follow established coding standards
- Include version control best practices

---

## Getting Help

For skill development questions:
- Check the skill documentation in each skill directory
- Review the skill examples in `.claude/skills/`
- Consult the Claude Code documentation
- Join the Wednesday Research Meetings