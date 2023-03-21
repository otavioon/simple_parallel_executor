import argparse
import yaml
import time
from pathlib import Path

def train(config, output_file):
    print(f"Train was called with config: {config}")
    print(f"All my outputs with be written to: {output_file}")
    # Write the config read from YAML file as a string in the output file
    print(config, file=output_file.open("w"))
    return 0

def main(args):
    # Configuration filename
    filename = Path(args.config_file)
    # Output directory
    output_dir = Path(args.output_dir)
    # Create the output directory if does not exist
    output_dir.mkdir(exist_ok=True, parents=True)
    # The output file location
    output_file = output_dir / filename.stem
    # Read the config
    config = yaml.safe_load(filename.open("r"))
    # Call train, with the config
    result = train(config, output_file)
    print(f"Done! Result: {result}\n")


if __name__=="__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--config-file", help="Path to the config file", required=True)
    parser.add_argument("--output-dir", help="The directory where outputs will be stored (the file name, in output directory, matches the configuration filaname", required=False, default="output")
    args = parser.parse_args()

    print(f"I was called with the args: {args}")
    main(args)
