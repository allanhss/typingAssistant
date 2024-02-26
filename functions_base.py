import inspect
import webbrowser


class FunctionBase:
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


class Text(FunctionBase):
    @staticmethod
    def lower(text):
        return text.lower()

    @staticmethod
    def upper(text):
        return text.upper()

    @staticmethod
    def camelCase(text):
        return "".join(word.capitalize() for word in text.split(" "))


class To(FunctionBase):
    @staticmethod
    def whatsAppContact(number):
        splited = [
            "".join(filter(str.isdigit, i))
            for i in number.replace("-", "").replace(")", " ").split(" ")
            if i
        ]
        print(splited)
        if len(splited) == 2:
            if len(splited[0]) not in [2, 3]:
                out = False
            elif len(splited[1]) not in [8, 9]:
                out = False
            else:
                splited[0] = splited[0].zfill(3)
                splited[1] = splited[1].zfill(9)
                out = "+55" + "".join(splited)
        elif len(splited) == 3:
            if len(splited[0]) > 2:
                out = False
            elif len(splited[1]) not in [2, 3]:
                out = False
            elif len(splited[2]) not in [8, 9]:
                out = False
            else:
                splited[0] = splited[0].zfill(2)
                splited[1] = splited[1].zfill(3)
                splited[2] = splited[2].zfill(9)
                out = "".join(splited)
        elif len(splited) == 1:
            if len(splited[0]) in [10, 11, 12]:
                out = "+55" + splited[0]
            elif len(splited[0]) in [12, 13, 14]:
                out = splited[0]
        else:
            out = False
        if out:
            webbrowser.open(f"wa.me/{out}")
        else:
            return False


class Obsidian(FunctionBase):
    @staticmethod
    def createGenericVmatrix(size):
        return (
            "$$\\begin{vmatrix}\n"
            + "\\\\\n".join(
                [
                    " & ".join([f"a_{{{i+1}{j+1}}}" for j in range(size)])
                    for i in range(size)
                ]
            )
            + "\n\\end{vmatrix}$$"
        )

    def createNullVmatrix(size):
        return (
            "$$\\begin{vmatrix}\n"
            + "\\\\\n".join(
                [" & ".join([f"0" for j in range(size)]) for i in range(size)]
            )
            + "\n\\end{vmatrix}$$"
        )

    def createIdentityVmatrix(size):
        return (
            "$$\\begin{vmatrix}\n"
            + "\\\\\n".join(
                [" & ".join([f"{int(i==j)}" for j in range(size)]) for i in range(size)]
            )
            + "\n\\end{vmatrix}$$"
        )


classes = [obj for name, obj in locals().items() if inspect.isclass(obj)]

if __name__ == "__main__":
    test = [
        "(74) 3614-7400",
        "07436147400",
        "074 36147400",
        "74 36-1400",
        "+55 074 3614-7400",
        "+55 (074)3614-7400",
    ]
    # print([To.whatsAppContact(i) for i in test])

    print(Obsidian.createNullVmatrix(4))
