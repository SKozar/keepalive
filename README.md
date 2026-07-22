# keepalive

Держит macOS «активной» для Teams в заданные часы. Дёргает мышь только при реальном простое системы.

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

- Раз в 30–60 секунд проверяет idle-таймер macOS
- Если простой > N секунд — сдвигает курсор на 1px (незаметно)
- Активен только в заданном окне (по умолчанию 04:00–12:00)
- Запускается как launchd-агент, переживает перезагрузку
