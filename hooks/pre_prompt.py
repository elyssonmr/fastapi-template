import sys
import subprocess

def is_docker_installed() -> bool:
    try:
        subprocess.run(["docker", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

if not is_docker_installed():
    print("ERROR: Docker is not installed.")
    print("Install it before proceeding.")
    sys.exit(1)
