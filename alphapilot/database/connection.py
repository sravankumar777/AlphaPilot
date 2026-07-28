"""
SQLite Database Connection module for AlphaPilot

This module is responsible for creating, managing the SQLite Database connection.
"""

import sqlite3
from pathlib import Path

def get_database_connection():
    """
    Create & return a connection to the SQLite Database.
    """

    # Project root directory
    project_root = Path(__file__).parent.parent

    # Database file location
    database_path = project_root / "database" / "alphapilot.db"

    # Create database connection
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    return connection


