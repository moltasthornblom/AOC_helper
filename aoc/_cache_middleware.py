"""Middleware for caching responses"""
import os
import hashlib
from decouple import config


def _cache_exists_or_create():
    if not os.path.exists(config("CACHE")):
        os.mkdir(config("CACHE"))
        return False
    return True


def _cache_file_exists(uri):
    if not _cache_exists_or_create():
        return False
    md5 = hashlib.md5(uri.encode()).hexdigest()
    for file in os.listdir(config("CACHE")):
        if os.fsdecode(file) == md5:
            with open(os.path.join(config("CACHE"), md5), "r", encoding="utf-8") as f:
                return f.read()
    return False


def _cache_save(uri, data):
    if not _cache_exists_or_create():
        return False
    md5 = hashlib.md5(uri.encode()).hexdigest()
    with open(os.path.join(config("CACHE"), md5), "w", encoding="utf-8") as f:
        f.write(data)
    return True


def _verbose_print(verbose, text):
    if verbose:
        print(text)


def _cache_request(request, *args, use_cache=True, verbose=False):
    """Caches arbitrary request. Returns tuple [status_code], [data]"""
    if not use_cache:
        _verbose_print(verbose, "Caching disabled. Performing Request...")
        return request(*args)
    cache = _cache_file_exists(args[0])
    if not cache:
        _verbose_print(verbose, "Cache not found. Performing Request...")
        response = request(*args)
        _cache_save(args[0], response[1])
        return response
    _verbose_print(verbose, "Caching exists. Using Cache...")
    return 200, cache
