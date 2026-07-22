# keepalive

Keep macOS "active" for Microsoft Teams during chosen hours. Moves the cursor only when the system is truly idle.


## Install

```bash
brew install skozar/tap/keepalive
```

## Usage

```bash
keepalive start --schedule 04:00-12:00 --idle 180
keepalive status
keepalive stop
```

## Build (dev)

```bash
make build           # PyInstaller → dist/keepalive
make release VERSION=1.0.0  # tag + push
```

## How it works

- Checks system idle time every 30–60 seconds
- If idle exceeds the configured threshold — moves the cursor by 1 px (imperceptible)
- Only active during the configured time window (default: 04:00–12:00)
- Runs as a launchd agent, survives reboots
