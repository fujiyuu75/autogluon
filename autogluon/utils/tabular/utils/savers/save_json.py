# TODO: Standardize / unify this code with ag.save()
import json
import os
import logging

logger = logging.getLogger(__name__)


# TODO: Support S3 paths
def save(path, obj, sanitize=True):
    if sanitize:
        obj = sanitize_object_to_primitives(obj=obj)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as fp:
        json.dump(obj, fp, indent=2)


def sanitize_object_to_primitives(obj):
    if isinstance(obj, dict):
        obj_sanitized = dict()
        for key, val in obj.items():
            obj_sanitized[key] = sanitize_object_to_primitives(val)
    else:
        try:
            json.dumps(obj)
            obj_sanitized = obj
        except (TypeError, OverflowError):
            json.dumps(type(obj).__name__)
            obj_sanitized = type(obj).__name__
    return obj_sanitized
