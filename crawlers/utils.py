# -*- coding: utf-8 -*-

import textwrap


def thread_info_to_dict(thread_info, nth=1, keys=list(), shorten_text=100):
    if not isinstance(thread_info, dict):
        return None

    if not (keys and isinstance(keys, list)):
        return None

    thread_string = f"{nth}).\n"
    for key in keys:
        content = thread_info[key]
        if isinstance(content, str):
            content = textwrap.shorten(content, width=shorten_text)
        thread_string += f"{key.upper()} : {content}\n"

    return thread_string


def concatenate_link(base_url, sub_link):
    if sub_link.find("https://") != -1:
        return sub_link
    return f"{base_url[:-1]}{sub_link}"
