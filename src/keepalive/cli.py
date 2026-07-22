"""CLI: start, stop, status, run."""

import argparse
import subprocess
import sys

from keepalive.config import (
    DEFAULT_SCHEDULE, DEFAULT_IDLE, DEFAULT_METHOD, DEFAULT_KEY,
    KEY_CODES, LAUNCHD_LABEL, LOG_FILE, PLIST_PATH,
)
from keepalive.daemon import daemon
from keepalive.log_config import log
from keepalive.plist import PLIST_TEMPLATE, binary_path, read_plist_config


# ── commands ────────────────────────────────────────────────────────────────

def cmd_start(schedule: str, idle: int, method: str, key: str):
    """Install and start the launchd agent."""
    if PLIST_PATH.exists():
        print("⚠️  Agent already installed. Run 'keepalive stop' first to reconfigure.")
        sys.exit(1)

    PLIST_PATH.parent.mkdir(parents=True, exist_ok=True)
    plist_xml = PLIST_TEMPLATE.format(
        label=LAUNCHD_LABEL,
        binary=binary_path(),
        schedule=schedule,
        idle=str(idle),
        method=method,
        key=key,
        log_file=str(LOG_FILE),
    )
    PLIST_PATH.write_text(plist_xml)
    subprocess.run(["launchctl", "load", str(PLIST_PATH)], check=True)
    log.info("Installed and started — schedule %s, idle %ds, method=%s, key=%s",
             schedule, idle, method, key)
    print(f"✅ Agent started — schedule {schedule}, idle {idle}s, method={method}"
          + (f", key={key}" if method in ("key", "both") else ""))
    print(f"   Logs: {LOG_FILE}")


def cmd_stop():
    """Unload and remove the launchd agent."""
    if PLIST_PATH.exists():
        subprocess.run(["launchctl", "unload", str(PLIST_PATH)], check=False)
        PLIST_PATH.unlink()
        log.info("Stopped and uninstalled")
        print("✅ Agent stopped")
    else:
        print("ℹ️  Agent is not installed")


def cmd_status():
    """Check if the launchd agent is loaded and show its configuration."""
    result = subprocess.run(
        ["launchctl", "list", LAUNCHD_LABEL],
        capture_output=True, text=True,
    )
    running = result.returncode == 0 and result.stdout.strip()

    cfg = read_plist_config()
    if running:
        print("🟢 keepalive is running")
    else:
        print("🔴 keepalive is not running")

    if cfg:
        method = cfg.get("method", DEFAULT_METHOD)
        extra = f", key={cfg['key']}" if method in ("key", "both") and "key" in cfg else ""
        print(f"   schedule : {cfg.get('schedule', DEFAULT_SCHEDULE)}")
        print(f"   idle     : {cfg.get('idle', str(DEFAULT_IDLE))}s")
        print(f"   method   : {method}{extra}")
    elif running:
        print("   (plist not found — settings unknown)")


def cmd_run(schedule: str, idle: int, method: str, key: str):
    """Run daemon in foreground for testing."""
    extra = f", key={key}" if method in ("key", "both") else ""
    print(f"🟢 Foreground mode — schedule {schedule}, idle {idle}s, method={method}{extra} (Ctrl+C to stop)")
    daemon(schedule, idle, method, key)


# ── argparse ────────────────────────────────────────────────────────────────

def _add_common_args(parser):
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE)
    parser.add_argument("--idle", type=int, default=DEFAULT_IDLE)
    parser.add_argument("--method", choices=("mouse", "key", "both"), default=DEFAULT_METHOD)
    parser.add_argument("--key", choices=list(KEY_CODES), default=DEFAULT_KEY)


def main():
    subcommands = {"start", "stop", "status", "run"}
    is_subcommand = len(sys.argv) > 1 and sys.argv[1] in subcommands

    if is_subcommand:
        cmd = sys.argv[1]
        parser = argparse.ArgumentParser(prog=f"keepalive {cmd}")
        if cmd == "start":
            _add_common_args(parser)
            args = parser.parse_args(sys.argv[2:])
            cmd_start(args.schedule, args.idle, args.method, args.key)
        elif cmd == "stop":
            cmd_stop()
        elif cmd == "status":
            cmd_status()
        elif cmd == "run":
            _add_common_args(parser)
            args = parser.parse_args(sys.argv[2:])
            cmd_run(args.schedule, args.idle, args.method, args.key)
    else:
        parser = argparse.ArgumentParser(prog="keepalive")
        _add_common_args(parser)
        args = parser.parse_args(sys.argv[1:])
        daemon(args.schedule, args.idle, args.method, args.key)
