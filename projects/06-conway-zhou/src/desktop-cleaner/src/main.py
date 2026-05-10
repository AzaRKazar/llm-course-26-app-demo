#!/usr/bin/env python3
import argparse
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import setup_logging



def run_gui():
    from PyQt5.QtWidgets import QApplication, QMessageBox
    from gui.app import MainWindow
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


def run_api():
    import uvicorn
    from api.server import app
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    setup_logging()

    parser = argparse.ArgumentParser(description="Desktop Cleaner")
    parser.add_argument("--mode", choices=["gui", "api"], default="gui")
    args = parser.parse_args()

    if args.mode == "api":
        run_api()
    else:
        run_gui()
