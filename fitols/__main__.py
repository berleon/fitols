from pathlib import Path

import savethat

if __name__ == "__main__":
    repro_dir = Path(__file__).parent.parent

    savethat.run_main("fitols")
