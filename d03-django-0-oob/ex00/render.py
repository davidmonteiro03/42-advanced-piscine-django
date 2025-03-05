#!/usr/bin/python3
import sys
import settings


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <template>")
        exit()
    try:
        template_path = sys.argv[1]
        if not template_path.endswith(".template"):
            raise Exception("Invalid extension")
        with open(template_path, "r") as template_file:
            template_content = template_file.read()
            template_file.close()
        html_path = f"""{template_path.removesuffix(".template")}.html"""
        with open(html_path, "w") as html_file:
            html_file.write(template_content.format(**settings.__dict__))
            html_file.close()
    except Exception as e:
        print(f"Error: {e}.", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
