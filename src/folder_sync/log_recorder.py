"""
Logging wrapper for Python logging module

This module provides an interface for configuring and using logs with
predefined formats, handlers (console and log file), and log levels.
It allows customization for the log file path in append mode.

"""

import functools
import logging
import types
import sys

def config_log(log_file):
    """
    Configure and return a logger with console and file output.

    Parameters
    ----------
    log_file : str
        Path to the log file (logs are always appended).

    Returns
    -------
    logging.Logger
        Logger instance with StreamHandler (stdout) and FileHandler.
    """
    logging.basicConfig(
        handlers = [
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, mode = "a"),
        ],
        level    = logging.INFO,
        encoding = "utf-8",
        format   = "{asctime} - {levelname} - {message}",
        style    = "{",
        datefmt  ="%Y-%m-%d %H:%M"
    )
    return logging.getLogger()

def decorate(module, decorator, *args):
    """
    Applies a decorator to all functions in a module.

    Args
    ----
        module (module): module object to decorate functions in.
        decorator (callable): Decorator function to apply (e.g., `log`).
        *args: Additional arguments to pass to the decorator.

    Returns
    -------
        None: Modifies the module in-place.
    """
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            setattr(module, name, decorator(obj, *args))

def log(func, log_file):
    """
    Decorator that logs function calls, arguments, returns, and exceptions.

    Parameters
    ----------
    func : callable
        Function to decorate.
    log_file : str
        Path to log file..

    Returns
    -------
    callable
        Wrapped function with logging behavior.
    """
    logger = config_log(log_file)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            logger.debug(str(result))
            return result
        except Exception as e:
            logger.warning(f"Exception: {str(e)} Raised in {func.__name__}.")
    return wrapper