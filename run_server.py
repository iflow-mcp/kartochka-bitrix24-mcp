#!/usr/bin/env python3
"""Wrapper script to run the FastMCP server"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.main import run

if __name__ == "__main__":
    run()