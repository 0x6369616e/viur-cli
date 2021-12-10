import typing
import os
import json
import click

from .utils import Singleton

CONF_PATH = "./viur.conf"


class Conf(Singleton, dict):
    def __init__(self, *args, **kwargs):
        super(dict).__init__(*args, **kwargs)
        super(Singleton).__init__()

        if os.path.exists(CONF_PATH):
            with open(CONF_PATH, "r") as f:
                data = json.load(f)
                for k, v in data.items():
                    super(dict, self).__setitem__(k, v)

    def set(self, k: typing.Any, v: typing.Any):
        save = True
        if k in self:
            if self[k] != v:
                self[k] = v
            else:
                save = False
        else:
            self.update({
                k: v
            })

        if save:
            self.save()

    def remove(self, k: typing.Any):
        if not self.get(k):
            return

        del self[k]
        self.save()

    def save(self, confirm: bool = False) -> None:
        if confirm:
            s = click.confirm("Do you really want the save the conf into the file?")
            if not s:
                return

        if not os.path.exists(CONF_PATH):
            os.mknod(CONF_PATH)

        with open(CONF_PATH, "w") as f:
            f.write(json.dumps(self, indent=4, sort_keys=True))


__all__ = ["Conf"]

if __name__ == "__main__":
    pass
