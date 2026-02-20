#!/usr/bin/env python3
"""
File System Watcher for Personal AI Employee
Monitors a drop folder for new files and creates action files
"""

import time
import logging
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from base_watcher import BaseWatcher

class DropFolderHandler(FileSystemEventHandler):
    def __init__(self, needs_action_path: Path):
        self.needs_action = needs_action_path

    def on_created(self, event):
        if event.is_directory:
            return

        source = Path(event.src_path)
        dest = self.needs_action / f"FILE_{source.name}"

        try:
            shutil.copy2(source, dest)
            self.create_metadata(source, dest)
        except Exception as e:
            logging.error(f"Error processing file {source.name}: {e}")

    def create_metadata(self, source: Path, dest: Path):
        meta_path = dest.with_suffix('.md')
        meta_content = f"""---
type: file_drop
original_name: {source.name}
size: {source.stat().st_size}
created: {datetime.now().isoformat()}
---

New file dropped for processing.

## File Details
- Original Name: {source.name}
- Size: {source.stat().st_size} bytes
- Created: {datetime.now().isoformat()}

## Suggested Actions
- [ ] Review file contents
- [ ] Process according to file type
- [ ] Move to appropriate folder after processing
- [ ] Archive original file if needed
"""
        meta_path.write_text(meta_content)

class FileSystemWatcher(BaseWatcher):
    def __init__(self, vault_path: str, watch_path: str, check_interval: int = 30):
        super().__init__(vault_path, check_interval)
        self.watch_path = Path(watch_path)
        self.observer = Observer()

    def check_for_updates(self):
        """Check for new files in the watch directory"""
        try:
            files = list(self.watch_path.glob('*'))
            new_files = [f for f in files if f.stat().st_ctime > time.time() - self.check_interval]

            self.logger.info(f"Found {len(new_files)} new files in {self.watch_path}")
            return new_files
        except Exception as e:
            self.logger.error(f"Error checking for updates: {e}")
            return []

    def create_action_file(self, file_path: Path):
        """Create action file for a new file"""
        try:
            content = f"""---
type: file_drop
original_name: {file_path.name}
size: {file_path.stat().st_size}
created: {datetime.now().isoformat()}
---

## File Dropped

New file detected: **{file_path.name}**

## File Details
- Size: {file_path.stat().st_size} bytes
- Created: {datetime.fromtimestamp(file_path.stat().st_ctime).isoformat()}

## Suggested Actions
- [ ] Review file contents
- [ ] Process according to file type
- [ ] Move to appropriate folder after processing
- [ ] Archive original file if needed
"""

            action_file = self.needs_action / f"FILE_{file_path.name}.md"
            action_file.write_text(content)
            self.logger.info(f"Created action file: {action_file.name}")
            return action_file

        except Exception as e:
            self.logger.error(f"Error creating action file for {file_path.name}: {e}")
            return None

    def run(self):
        """Start the file system watcher"""
        # Setup the observer
        event_handler = DropFolderHandler(self.needs_action)
        self.observer.schedule(event_handler, str(self.watch_path), recursive=False)
        self.observer.start()

        try:
            self.logger.info(f"Starting file system watcher on {self.watch_path}...")
            while True:
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    # Configuration - update these paths
    VAULT_PATH = "C:\\Users\\rehman\\hackathon-0\\bronze-tier\\AI_Employee_Vault"
    WATCH_PATH = "C:\\Users\\rehman\\Downloads\\AI_Employee_Drop"  # Change to your drop folder

    # Create watch directory if it doesn't exist
    Path(WATCH_PATH).mkdir(parents=True, exist_ok=True)

    # Initialize and run watcher
    watcher = FileSystemWatcher(VAULT_PATH, WATCH_PATH)
    watcher.run()