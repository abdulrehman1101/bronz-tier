#!/usr/bin/env python3
"""
Gmail Watcher for Personal AI Employee Hackathon
Monitors Gmail for new messages and creates action files in Obsidian vault
"""

import time
import logging
import json
from pathlib import Path
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class GmailWatcher:
    def __init__(self, vault_path: str, credentials_path: str, check_interval: int = 120):
        self.vault_path = Path(vault_path)
        self.needs_action = self.vault_path / "Needs_Action"
        self.check_interval = check_interval
        self.processed_ids = set()

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.vault_path / "Logs" / "gmail_watcher.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger("GmailWatcher")

        # Load credentials
        self.creds = Credentials.from_authorized_user_file(credentials_path)
        self.service = build('gmail', 'v1', credentials=self.creds)

        # Load previously processed message IDs
        self.load_processed_ids()

    def load_processed_ids(self):
        """Load previously processed message IDs from log file"""
        log_file = self.vault_path / "Logs" / "processed_ids.json"
        if log_file.exists():
            try:
                with open(log_file, 'r') as f:
                    data = json.load(f)
                    self.processed_ids = set(data.get('processed_ids', []))
                self.logger.info(f"Loaded {len(self.processed_ids)} previously processed IDs")
            except Exception as e:
                self.logger.warning(f"Could not load processed IDs: {e}")

    def save_processed_ids(self):
        """Save processed message IDs to log file"""
        log_file = self.vault_path / "Logs" / "processed_ids.json"
        try:
            with open(log_file, 'w') as f:
                json.dump({"processed_ids": list(self.processed_ids)}, f)
        except Exception as e:
            self.logger.warning(f"Could not save processed IDs: {e}")

    def check_for_updates(self):
        """Check for new unread messages in Gmail"""
        try:
            results = self.service.users().messages().list(
                userId='me', q='is:unread is:important'
            ).execute()
            messages = results.get('messages', [])
            new_messages = [m for m in messages if m['id'] not in self.processed_ids]

            self.logger.info(f"Found {len(messages)} unread messages, {len(new_messages)} new")
            return new_messages

        except Exception as e:
            self.logger.error(f"Error checking Gmail: {e}")
            return []

    def create_action_file(self, message):
        """Create Obsidian action file for a Gmail message"""
        try:
            msg = self.service.users().messages().get(
                userId='me', id=message['id']
            ).execute()

            # Extract headers
            headers = {h['name']: h['value'] for h in msg['payload']['headers']}

            content = f"""---
type: email
from: {headers.get('From', 'Unknown')}
subject: {headers.get('Subject', 'No Subject')}
received: {datetime.now().isoformat()}
priority: high
status: pending
---

## Email Content
{msg.get('snippet', 'No content available')}

## Suggested Actions
- [ ] Reply to sender
- [ ] Forward to relevant party
- [ ] Archive after processing
- [ ] Flag for follow-up if needed
"""

            filepath = self.needs_action / f"EMAIL_{message['id']}.md"
            filepath.write_text(content)

            self.processed_ids.add(message['id'])
            self.save_processed_ids()

            self.logger.info(f"Created action file: {filepath.name}")
            return filepath

        except Exception as e:
            self.logger.error(f"Error creating action file for message {message['id']}: {e}")
            return None

    def run(self):
        """Main loop for the Gmail watcher"""
        self.logger.info("Starting Gmail Watcher...")

        while True:
            try:
                items = self.check_for_updates()
                for item in items:
                    self.create_action_file(item)
            except Exception as e:
                self.logger.error(f"Error in main loop: {e}")

            time.sleep(self.check_interval)

if __name__ == "__main__":
    # Configuration - update these paths
    VAULT_PATH = "C:\\Users\\rehman\\hackathon-0\\bronze-tier\\AI_Employee_Vault"
    CREDENTIALS_PATH = "C:\\path\\to\\gmail_credentials.json"

    # Create vault directories if they don't exist
    Path(VAULT_PATH).mkdir(parents=True, exist_ok=True)
    (Path(VAULT_PATH) / "Needs_Action").mkdir(exist_ok=True)
    (Path(VAULT_PATH) / "Logs").mkdir(exist_ok=True)

    # Initialize and run watcher
    watcher = GmailWatcher(VAULT_PATH, CREDENTIALS_PATH)
    watcher.run()