#!/usr/bin/env python3
"""
Base Watcher Template for Personal AI Employee
Provides common functionality for all watcher scripts
"""

import time
import logging
from pathlib import Path
from abc import ABC, abstractmethod

class BaseWatcher(ABC):
    def __init__(self, vault_path: str, check_interval: int = 60):
        self.vault_path = Path(vault_path)
        self.needs_action = self.vault_path / 'Needs_Action'
        self.check_interval = check_interval

        # Create directories if they don't exist
        self.needs_action.mkdir(parents=True, exist_ok=True)

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.vault_path / "Logs" / f"{self.__class__.__name__}.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def check_for_updates(self) -> list:
        '''Return list of new items to process'''
        pass

    @abstractmethod
    def create_action_file(self, item) -> Path:
        '''Create .md file in Needs_Action folder'''
        pass

    def run(self):
        """Main loop for the watcher"""
        self.logger.info(f'Starting {self.__class__.__name__}...')

        while True:
            try:
                items = self.check_for_updates()
                for item in items:
                    self.create_action_file(item)
            except Exception as e:
                self.logger.error(f'Error: {e}')

            time.sleep(self.check_interval)

    def create_metadata_file(self, filepath: Path, metadata: dict):
        """Create a metadata file with additional information"""
        meta_filepath = filepath.with_suffix('.md')
        meta_content = f"""---
{self._format_metadata(metadata)}
---

{metadata.get('description', 'No description available')}
"""
        meta_filepath.write_text(meta_content)
        self.logger.info(f"Created metadata file: {meta_filepath.name}")

    def _format_metadata(self, metadata: dict) -> str:
        """Format metadata dictionary as YAML"""
        lines = []
        for key, value in metadata.items():
            if isinstance(value, str):
                lines.append(f"{key}: {value}")
            else:
                lines.append(f"{key}: {json.dumps(value)}")
        return "\n".join(lines)