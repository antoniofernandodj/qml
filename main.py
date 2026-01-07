import importlib
import sys
if len(sys.argv) < 2:
    raise SystemExit("Uso: python main.py <example>")



def main():

    try:
        module = importlib.import_module(f"{sys.argv[1]}.main")
    except ModuleNotFoundError as e:
        raise SystemExit(f"Example inválido: {sys.argv[1]}") from e

    module.main()


if __name__ == "__main__":
    main()
