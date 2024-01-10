import inspect


class Function:
    @classmethod
    def getFunctionsDict(cls):
        cls_name = cls.__name__
        functions_dict = {
            f"{cls_name}.{name}": method
            for name, method in inspect.getmembers(cls, predicate=inspect.isfunction)
        }
        if f"{cls_name}.getFunctionsDict" in functions_dict:
            del functions_dict[f"{cls_name}.getFunctionsDict"]
        return functions_dict


class Text(Function):
    @staticmethod
    def lower(text):
        return text.lower()

    @staticmethod
    def upper(text):
        return text.upper()

    @staticmethod
    def camelCase(text):
        return "".join(word.capitalize() for word in text.split(" "))


class To(Function):
    @staticmethod
    def whatsAppContact(number):
        print(f"WppContact -> {number}")


classes = [obj for name, obj in locals().items() if inspect.isclass(obj)]
