# Reporting

A lightweight, reusable reporting framework for Python applications.

The Reporting module provides a consistent, configurable, and application-independent interface for publishing runtime information. It abstracts formatting, output routing, and report generation behind a small public API, allowing applications to focus on **what** should be reported rather than **how** it should be presented.

The framework is suitable for CLI tools, automation pipelines, long-running services, developer tooling, and any application requiring structured runtime reporting.

---

# Features

- Simple public API
- Configurable report formatting
- Terminal and log output support
- Runtime message tagging
- Configurable timestamp formatting
- Structured report layouts
- Reusable across applications
- Consistent reporting style
- Separation of reporting logic from application logic

---

# Design Philosophy

The Reporting framework is built around a simple principle:

> Applications should publish reports, not construct them.

Application code interacts exclusively with the `ReportingManager`.

The reporting subsystem owns:

- Report formatting
- Report structure
- Timestamp generation
- Heading generation
- Output routing
- Log publishing

This keeps application code clean while allowing the reporting subsystem to evolve independently.

---

# Getting Started

Create a reporting manager.

```python
from reporting.reporting_manager import ReportingManager

reporting = ReportingManager()
```

The `ReportingManager` is the only public entry point into the reporting subsystem.

---

# Public API

The ReportingManager intentionally exposes a small API surface.

| Method         | Purpose                         |
| -------------- | ------------------------------- |
| `header()`     | Publish a major section heading |
| `sub_header()` | Publish a subsection heading    |
| `timestamp()`  | Publish a formatted timestamp   |
| `message()`    | Publish runtime information     |

---

# Header

Publishes a major report section.

```python
reporting.header(
    title="Scanner"
)
```

Typical use cases

- Module execution
- Pipeline stages
- Report sections
- High-level operations

---

## Parameters

| Parameter     | Type                | Default       | Description        |
| ------------- | ------------------- | ------------- | ------------------ |
| `title`       | `str`               | Required      | Heading text       |
| `destination` | `ReportDestination` | `LOG`         | Output destination |
| `log_type`    | `LogType`           | `OPERATIONAL` | Log category       |

---

# Sub Header

Publishes a subsection heading.

```python
reporting.sub_header(
    title="Directory Scan"
)
```

Typical use cases

- Execution phases
- Validation steps
- Nested report sections

---

## Parameters

| Parameter     | Type                | Default       | Description        |
| ------------- | ------------------- | ------------- | ------------------ |
| `title`       | `str`               | Required      | Subsection title   |
| `destination` | `ReportDestination` | `LOG`         | Output destination |
| `log_type`    | `LogType`           | `OPERATIONAL` | Log category       |

---

# Timestamp

Publishes the current timestamp.

```python
reporting.timestamp()
```

The timestamp API allows applications to customize the content, formatting, and presentation of timestamps.

---

## Parameters

| Parameter          | Type                | Default           | Description                          |
| ------------------ | ------------------- | ----------------- | ------------------------------------ |
| `timestamp_type`   | `TimestampType`     | Framework default | Timestamp content                    |
| `timestamp_format` | `TimestampFormat`   | Framework default | Display style                        |
| `component_gap`    | `int`               | Framework default | Spacing between timestamp components |
| `destination`      | `ReportDestination` | `LOG`             | Output destination                   |
| `log_type`         | `LogType`           | `OPERATIONAL`     | Log category                         |

---

## Timestamp Types

Determines which time information is displayed.

| Value                     | Description   | Example               |
| ------------------------- | ------------- | --------------------- |
| `TimestampType.TIME`      | Time only     | `14:52:18`            |
| `TimestampType.DATE`      | Date only     | `2026-07-23`          |
| `TimestampType.DATE_TIME` | Date and time | `2026-07-23 14:52:18` |

Example

```python
reporting.timestamp(
    timestamp_type=TimestampType.TIME
)
```

---

## Timestamp Formats

Controls how the timestamp is rendered.

| Value           | Description                         | Example                 |
| --------------- | ----------------------------------- | ----------------------- |
| `STANDARD`      | Standard formatting                 | `2026-07-23 14:52:18`   |
| `BRACKETED`     | Surround timestamp with brackets    | `[2026-07-23 14:52:18]` |
| `PARENTHESIZED` | Surround timestamp with parentheses | `(2026-07-23 14:52:18)` |

Example

```python
reporting.timestamp(
    timestamp_format=TimestampFormat.BRACKETED
)
```

---

## Component Gap

Controls spacing between individual timestamp components.

Example

```python
reporting.timestamp(
    component_gap=4
)
```

Useful for:

- Dashboard style output
- Readability improvements
- Custom console layouts

---

# Message

Publishes runtime information.

```python
reporting.message(
    message="Scanner execution started."
)
```

This is the primary reporting method and supports multiple optional formatting features.

---

## Parameters

| Parameter     | Type                | Default       | Description                    |
| ------------- | ------------------- | ------------- | ------------------------------ |
| `message`     | `str`               | Required      | Report text                    |
| `timestamp`   | `bool`              | `False`       | Include timestamp              |
| `tag`         | `str`               | `None`        | Module or component identifier |
| `data_items`  | `list[MessageData]` | `None`        | Structured message data        |
| `destination` | `ReportDestination` | `LOG`         | Output destination             |
| `log_type`    | `LogType`           | `OPERATIONAL` | Log category                   |

---

## Basic Message

```python
reporting.message(
    message="Planning completed."
)
```

Example output

```
Planning completed.
```

---

## Timestamped Message

```python
reporting.message(
    message="Planning completed.",
    timestamp=True,
)
```

Example output

```
[14:52:18] Planning completed.
```

Recommended for

- Runtime monitoring
- Debugging
- Execution tracing

---

## Tagged Message

```python
reporting.message(
    tag="Planner",
    message="Planning completed."
)
```

Example output

```
[Planner] Planning completed.
```

Recommended for

- Multi-module applications
- Log readability
- Component identification

---

## Timestamped Tagged Message

```python
reporting.message(
    timestamp=True,
    tag="Planner",
    message="Planning completed."
)
```

Example output

```
[14:52:18] [Planner] Planning completed.
```

Recommended for operational logging.

---

# Report Destination

Determines where reports are published.

| Value                        | Description                  | Typical Use                  |
| ---------------------------- | ---------------------------- | ---------------------------- |
| `ReportDestination.TERMINAL` | Publish only to the terminal | Interactive CLI applications |
| `ReportDestination.LOG`      | Publish only to log files    | Background execution         |
| `ReportDestination.ALL`      | Publish to terminal and logs | Development and monitoring   |

Example

```python
reporting.message(
    message="Execution completed.",
    destination=ReportDestination.ALL,
)
```

---

# Log Types

Classifies persisted log entries.

| Value                 | Description                   | Typical Use                   |
| --------------------- | ----------------------------- | ----------------------------- |
| `LogType.OPERATIONAL` | Normal application execution  | Runtime operations            |
| `LogType.DIAGNOSTIC`  | Diagnostic information        | Debugging and troubleshooting |
| `LogType.ALL`         | Applies to all log categories | Internal or framework use     |

Example

```python
reporting.message(
    message="Connection established.",
    log_type=LogType.OPERATIONAL,
)
```

---

# Common Usage Patterns

## Simple Status Update

```python
reporting.message(
    message="Application started."
)
```

---

## Module Execution

```python
reporting.header(
    title="Scanner"
)

reporting.message(
    timestamp=True,
    tag="Scanner",
    message="Scanning directory."
)
```

---

## Complete Execution Flow

```python
reporting.header(
    title="Planner"
)

reporting.sub_header(
    title="Packet Generation"
)

reporting.message(
    timestamp=True,
    tag="Planner",
    message="Planning started."
)

reporting.message(
    timestamp=True,
    tag="Planner",
    message="Planning completed."
)
```

---

# Configuration Reference

| Feature          | Supported Options                  |
| ---------------- | ---------------------------------- |
| Heading Type     | Header, Sub Header                 |
| Timestamp Type   | Date, Time, Date & Time            |
| Timestamp Format | Standard, Bracketed, Parenthesized |
| Destination      | Terminal, Log, All                 |
| Log Type         | Operational, Diagnostic, All       |

---

# Best Practices

- Create a single `ReportingManager` instance per application.
- Use `header()` to divide major execution stages.
- Use `sub_header()` for nested report sections.
- Use timestamps for execution tracing.
- Use tags to identify reporting modules.
- Route reports through destinations instead of printing directly.
- Prefer consistent tagging across the application.
- Use operational logs for normal execution and diagnostic logs for troubleshooting.

---

# Public API Boundary

Applications should interact only with the `ReportingManager`.

The reporting framework owns all formatting, routing, and presentation logic internally.

This abstraction allows applications to remain independent of the reporting implementation while ensuring a consistent reporting experience.

---

# Future Direction

The Reporting framework is designed to evolve without requiring changes to application code.

Additional formatting capabilities, destinations, and reporting features will continue to be introduced through the existing public API, preserving backward compatibility while expanding functionality.
