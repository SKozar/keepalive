# keepalive

[![tests](https://github.com/skozar/keepalive/actions/workflows/test.yml/badge.svg)](https://github.com/skozar/keepalive/actions/workflows/test.yml)
[![coverage](https://img.shields.io/badge/coverage-available-success)](https://github.com/skozar/keepalive/actions/workflows/test.yml)

Stay green. Simulates macOS input activity only when you're away — so messaging apps don't mark you as "Away" or "Idle."

## What it solves

Slack, Discord, Microsoft Teams, and Mattermost all detect user presence through macOS idle time. After 5–10 minutes of inactivity, they switch your status to "Away." keepalive resets the idle timer by moving the cursor a pixel or pressing a harmless key — imperceptible, only when the system is genuinely idle, and only during your configured hours.

| App | Away after |
|---|---|
| Slack | ~10 min |
| Discord | ~5 min |
| Microsoft Teams | ~5 min |
| Mattermost | configurable |

### What it will NOT do

- Prevent display sleep — use `caffeinate` or Amphetamine
- Simulate activity in browser-based apps (Figma, Google Docs) — they use DOM events, not macOS idle
- Keep SSH or VPN sessions alive — use protocol-level keepalives
- Work on cloud VMs without a GUI

## Install

```bash
brew tap skozar/tap
brew trust skozar/tap
brew install keepalive
```

Grant Accessibility permission: System Settings → Privacy & Security → Accessibility → add `/opt/homebrew/opt/keepalive/bin/keepalive`.

## Usage

```bash
# Mouse jiggle (default)
keepalive start --schedule 04:00-12:00 --idle 180

# Key press (F13)
keepalive start --method key

# Both — maximum reliability
keepalive start --method both --key f14

# Check status and settings
keepalive status

# Stop and uninstall
keepalive stop
```

| Option | Values | Default | Description |
|---|---|---|---|
| `--schedule` | `HH:MM-HH:MM` | `04:00-12:00` | Active time window |
| `--idle` | seconds | `180` | Idle threshold before firing |
| `--method` | `mouse`, `key`, `both` | `mouse` | How to reset idle timer |
| `--key` | `f13`, `f14`, `f15` | `f13` | Key to press (when using `key`/`both`) |

## How it works

- Checks system idle time via Quartz every 30–60 seconds
- If idle exceeds the configured threshold and current time is within the active window — fires the chosen method
- When using `both`, mouse jiggle and key press run with a 50ms gap (two separate HID events)
- Runs as a launchd agent, survives reboots
- Logs to `~/Library/Logs/keepalive/keepalive.log` (auto-rotated, 5 × 1 MB)

## Build (dev)

```bash
make build                       # PyInstaller → dist/keepalive
make release VERSION=0.2.1       # Build, tag, release, update homebrew-tap
```
