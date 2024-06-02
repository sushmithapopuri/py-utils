from json import *
import os

# SEPARATOR = '.'


def _get_keys(jobject, depth, separator, flatten_list, curr_depth=0, key_list=[]):
    curr_depth = curr_depth + 1
    for key, val in jobject.items():
        if (
            flatten_list
            and isinstance(val, list)
            and (depth == 0 or (depth > 0 and curr_depth < depth))
        ):
            for i, item in enumerate(val):
                yield from _get_keys(
                    item,
                    depth,
                    separator,
                    flatten_list,
                    curr_depth,
                    key_list + [key + "{}[{}]".format(separator, i)],
                )

        elif isinstance(val, dict) and (
            depth == 0 or (depth > 0 and curr_depth < depth)
        ):
            yield from _get_keys(
                val, depth, separator, flatten_list, curr_depth, key_list + [key]
            )

        else:
            yield separator.join(key_list + [key])


def get_keys(jobject, depth=0, separator=".", flatten_list=True):
    keys = []
    if isinstance(jobject, dict):
        keys = [*_get_keys(jobject, depth, separator, flatten_list)]
    if isinstance(jobject, list):
        for i, item in enumerate(jobject):
            keys.extend(
                [*_get_keys({"[{}]".format(i): item}, depth, separator, flatten_list)]
            )
    if isinstance(jobject, str):
        keys = [*_get_keys(loads(jobject), depth, separator, flatten_list)]
    return keys


def get(jobject, key, separator="."):
    keys = key.split(separator)
    object = jobject
    try:
        for tag in keys:
            if tag[0] == "[" and tag[-1] == "]":
                tag = int(tag.replace("[", "").replace("]", ""))
            object = object[tag]
        return object
    except Exception as exception:
        print(exception)


def put(jobject, key, val, separator="."):
    keys = key.split(separator)
    data = jobject
    try:
        for tag in keys:
            if tag[0] == "[" and tag[-1] == "]":
                tag = int(tag.replace("[", "").replace("]", ""))
            if tag not in data:
                data[tag]
            data = data[tag]
        return data
    except Exception as exception:
        print(exception)


def _flatten(
    jobject, depth, separator, flatten_list, curr_depth=0, key_list=[], data={}
):

    if isinstance(jobject, dict):
        curr_depth = curr_depth + 1
        for key, val in jobject.items():
            if (
                flatten_list
                and isinstance(val, list)
                and (depth == 0 or (depth > 0 and curr_depth < depth))
            ):
                for i, item in enumerate(val):
                    yield from _flatten(
                        item,
                        depth,
                        separator,
                        flatten_list,
                        curr_depth,
                        key_list + [key + "{}[{}]".format(separator, i)],
                    )

            elif isinstance(val, dict) and (
                depth == 0 or (depth > 0 and curr_depth < depth)
            ):
                yield from _flatten(
                    val, depth, separator, flatten_list, curr_depth, key_list + [key]
                )

            else:
                yield {separator.join(key_list + [key]): val}
    else:
        print("Cannot Flatten further")


def flatten(jobject, depth = 0, separator=".", flatten_list=True):
    data = []
    if isinstance(jobject, dict):
        data = [*_flatten(jobject, depth, separator, flatten_list)]
    if flatten_list and isinstance(jobject, list):
        for i, item in enumerate(jobject):
            data.extend(
                [*_flatten({"[{}]".format(i): item}, depth, separator, flatten_list)]
            )
    if isinstance(jobject, str):
        data = [*_flatten(loads(jobject), depth, separator, flatten_list)]
    return {k: v for item in data for k, v in item.items()}


def _nest(jobject, depth, separator, curr_depth=0, key_list=[], data={}):

    if isinstance(jobject, dict):
        curr_depth = curr_depth + 1
        for key, val in jobject.items():
            yield {separator.join(key_list + [key]): val}
    else:
        print("Cannot Nest further")


def nest(jobject, depth, separator="."):
    data = dict()
    lists = ([*k.split(separator), v] for k, v in jobject.items())
    for lst in lists:
        for x in lst[:-2]:
            data[x] = data = data.get(x, dict())
            data.update({lst[-2]: lst[-1]})
    return data
