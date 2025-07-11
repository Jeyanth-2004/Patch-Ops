from typing import Dict, List
import os
from .config import SOFTWARE_SCAN_FILE, WINDOWS_SCAN_FILE
from .software_scanner import parse_software_vulnerabilities
from .windows_scanner import parse_windows_vulnerabilities
from .utils import run_scanner_script, ensure_output_dir

class ScanManager:
    def __init__(self):
        ensure_output_dir()
        
    def run_scans(self) -> bool:
        """Run both scanner scripts"""
        scripts = [
            'softwarepatch.py',
            'windowspatch.py'
        ]
        
        return all(run_scanner_script(script) for script in scripts)
    
    def get_results(self) -> Dict[str, List[Dict]]:
        """Get combined scan results"""
        return {
            'software': parse_software_vulnerabilities(SOFTWARE_SCAN_FILE),
            'windows': parse_windows_vulnerabilities(WINDOWS_SCAN_FILE)
        }
