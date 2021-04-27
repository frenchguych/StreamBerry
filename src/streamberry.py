from os import environ
import os.path

from streamberry.engine import StreamBerryEngine

if __name__ == '__main__':
    engine = StreamBerryEngine()

    config_files = [file for file in [
        "streamberry.yaml", f"{environ['HOME']}/.streamberry/streamberry.yaml"] if os.path.exists(file)]
    if "SNAP_USER_COMMON" in environ:
        config_file = os.path.join(environ['SNAP_USER_COMMON'], 'streamberry.yaml')
        if os.path.exists((config_file)):
            config_files.append(config_file)

    if len(config_files) == 0:
        raise FileNotFoundError("streamberry.yaml")
    engine.init(config_files[0])
    engine.run()
