import inspect


class Text:
    @staticmethod
    def lower(text):
        return text.lower()

    @staticmethod
    def upper(text):
        return text.upper()

    @staticmethod
    def getFunctionsDict():
        functions_dict = {
            f"Text.{name}": method
            for name, method in inspect.getmembers(Text, predicate=inspect.isfunction)
        }
        del functions_dict[
            "Text.getFunctionsDict"
        ]  # Remove a função getFunctionsDict do dicionário
        return functions_dict
