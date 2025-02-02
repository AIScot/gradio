from __future__ import annotations

import warnings

from gradio import utils


class GradioDeprecationWarning(UserWarning):
    # This does not subclass DeprecationWarning
    # because we want to show the warning by default.
    pass


def simple_deprecated_notice(term: str) -> str:
    return f"`{term}` parameter is deprecated, and it has no effect"


def use_in_launch(term: str) -> str:
    return f"`{term}` is deprecated in `Interface()`, please use it within `launch()` instead."


DEPRECATION_MESSAGE = {
    "optional": simple_deprecated_notice("optional"),
    "keep_filename": simple_deprecated_notice("keep_filename"),
    "numeric": simple_deprecated_notice("numeric"),
    "verbose": simple_deprecated_notice("verbose"),
    "allow_screenshot": simple_deprecated_notice("allow_screenshot"),
    "layout": simple_deprecated_notice("layout"),
    "show_input": simple_deprecated_notice("show_input"),
    "show_output": simple_deprecated_notice("show_output"),
    "capture_session": simple_deprecated_notice("capture_session"),
    "api_mode": simple_deprecated_notice("api_mode"),
    "show_tips": use_in_launch("show_tips"),
    "encrypt": simple_deprecated_notice("encrypt"),
    "enable_queue": use_in_launch("enable_queue"),
    "server_name": use_in_launch("server_name"),
    "server_port": use_in_launch("server_port"),
    "width": use_in_launch("width"),
    "height": use_in_launch("height"),
    "plot": "The 'plot' parameter has been deprecated. Use the new Plot component instead",
    "type": "The 'type' parameter has been deprecated. Use the Number component instead.",
}


def check_deprecated_parameters(
    cls: str, *, stacklevel: int | None = None, kwargs
) -> None:
    if stacklevel is None:
        stacklevel = utils.find_user_stack_level()

    for key, value in DEPRECATION_MESSAGE.items():
        if key in kwargs:
            kwargs.pop(key)
            warnings.warn(value, GradioDeprecationWarning, stacklevel=stacklevel)

    if kwargs:
        warnings.warn(
            f"You have unused kwarg parameters in {cls}, please remove them: {kwargs}",
            GradioDeprecationWarning,
            stacklevel=stacklevel,
        )


def warn_deprecation(text: str) -> None:
    warnings.warn(
        text,
        GradioDeprecationWarning,
        stacklevel=utils.find_user_stack_level(),
    )


def warn_style_method_deprecation() -> None:
    warn_deprecation(
        "The `style` method is deprecated. Please set these arguments in the constructor instead."
    )
