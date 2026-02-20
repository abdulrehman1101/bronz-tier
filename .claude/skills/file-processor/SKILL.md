# File Processing Skill

## Purpose
Handle files dropped in the monitoring folder and create appropriate action items.

## Inputs
- Files in drop folder
- File metadata and properties
- File type and content analysis

## Outputs
- Action files in Needs_Action folder
- File processing instructions
- Metadata documentation

## Dependencies
- File system monitoring
- File type detection
- Content analysis capabilities

## Security Considerations
- Validate all file types
- Scan for malicious content
- Respect file permissions
- Log all file operations

## Usage

### Basic Usage
```
claude --skill file-processor
```

### With Custom Configuration
```
claude --skill file-processor --drop-folder /path/to/drop
```

## Examples

### Process New Files
```
claude --skill file-processor --scan-folder
```

### Process Specific File
```
claude --skill file-processor --file /path/to/file.txt
```