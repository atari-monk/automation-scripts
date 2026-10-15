## What it does

```python
logger.setLevel(logging.DEBUG)
```

It tells the logger: _"Process every log message at DEBUG level or higher."_

## Logging levels (low → high)

| Level      | Numeric value | Purpose                              |
| ---------- | ------------- | ------------------------------------ |
| `DEBUG`    | 10            | Detailed diagnostic info             |
| `INFO`     | 20            | Confirmation things work normally    |
| `WARNING`  | 30            | Something unexpected (default level) |
| `ERROR`    | 40            | Serious problem                      |
| `CRITICAL` | 50            | Fatal error                          |

## Key behavior

Any message **below** the set level is **ignored**.

```python
logger.setLevel(logging.DEBUG)

logger.debug("x = 5")      # ✅ logged
logger.info("started")     # ✅ logged
logger.warning("careful")  # ✅ logged
logger.error("failed")     # ✅ logged
```

vs.

```python
logger.setLevel(logging.WARNING)

logger.debug("x = 5")      # ❌ ignored
logger.info("started")     # ❌ ignored
logger.warning("careful")  # ✅ logged
logger.error("failed")     # ✅ logged
```

## ⚠️ Common gotcha

Setting the logger level alone often isn't enough — **handlers** have their own levels too:

```python
logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)   # also needed, otherwise handler filters
```

The effective level is the **more restrictive** of the logger and its handlers. Also, if a logger has no level set, it inherits from its parent (ultimately the root logger, which defaults to `WARNING`).

So `logger.setLevel(logging.DEBUG)` = "show me everything from DEBUG upward, at this logger."
