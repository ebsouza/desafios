import textwrap


def print_threads(threads_list, keys=list(), shorten_text=100):
    if not (keys and isinstance(keys, list)):
        return None

    counter = 0
    print("-------------")
    for thread in threads_list:
        counter += 1
        print(f"{counter}).")
        for key in keys:
            content = thread[key]
            if isinstance(content, str):
                content = textwrap.shorten(content, width=shorten_text)
            print(f"{key.upper()} : {content}")
    print("------------")


def concatenate_link(base_url, sub_link):
    if sub_link.find("https://") != -1:
        return sub_link
    return f"{base_url[:-1]}{sub_link}"
