# Task Planning Skill

## Purpose
Create comprehensive action plans for complex tasks from the Needs_Action folder.

## Inputs
- Items in Needs_Action folder
- Company_Handbook rules and guidelines
- Current system state from Dashboard

## Outputs
- Detailed plans in Plans folder
- Step-by-step action items
- Priority levels and timelines
- Required approvals

## Dependencies
- Access to Needs_Action folder
- Understanding of Company_Handbook
- Dashboard for current context

## Security Considerations
- Read-only access to Needs_Action items
- Write access to Plans folder
- No external data access required

## Usage

### Basic Usage
```
claude --skill task-planner
```

### With Custom Parameters
```
claude --skill task-planner --folder Needs_Action --plan-folder Plans
```

## Examples

### Plan All Pending Tasks
```
claude --skill task-planner --plan-all
```

### Create Plan for Specific Item
```
claude --skill task-planner --item NEEDS-123 --create-plan
```