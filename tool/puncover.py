from flask import Flask
from collector import Collector
import renderers

def build_collector(pebble_sdk, project_dir=None, elf_file=None, su_dir=None):
    c = Collector(pebble_sdk=pebble_sdk)
    if project_dir:
        # TODO: check if this is a pebble project dir
        c.parse_pebble_project_dir(project_dir)
    if elf_file:
        c.parse(elf_file, su_dir)

    c.enhance()
    return c


app = Flask(__name__)

if __name__ == '__main__':

    # TODO: extract into CLI args
    pebble_sdk = "/Users/behrens/pebble-dev/PebbleSDK-current"

    project_dir = "/Users/behrens/Documents/projects/pebble/puncover/pebble"
    # project_dir = "/Users/behrens/Documents/projects/pebble/PinyWings/pebble-2/PinyWings"
    # project_dir = "/Users/behrens/Documents/projects/pebble/pebble-tinymath"
    collector = build_collector(project_dir=project_dir, pebble_sdk=pebble_sdk)


    # elf_file = "/Users/behrens/Documents/projects/pebble/tintin/build/src/fw/tintin_fw.elf"
    # collector = build_collector(elf_file=elf_file, pebble_sdk=pebble_sdk)


    renderers.register_jinja_filters(app.jinja_env)
    renderers.register_urls(app, collector)

    app.run(debug=True)
