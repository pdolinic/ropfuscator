from typing import List


OUTFILE = "gadgets.asm"

REG2REG_OP = ["xor", "and", "or", "mov"]
REGONLY_OP = ["push", "pop"]

X86_REGS = ["eax", "ebx", "ecx", "edx", "esi", "edi", "esp", "ebp"]


def export_directive_template(name):
    return f"global {name}"


def code_template(symname, operation):
    return f"""{symname}:  {operation}\n\tret"""


def main():
    exports: List[str] = []
    functions: List[str] = []

    for op in REG2REG_OP:
        for dst in X86_REGS:
            for src in X86_REGS:
                symname = f"{op}_{dst}_{src}"
                exports.append(export_directive_template(symname))
                functions.append(code_template(symname, f"{op} {dst}, {src}"))

    for op in REGONLY_OP:
        for r in X86_REGS:
            symname = f"{op}_{r}"
            exports.append(export_directive_template(symname))
            functions.append(code_template(symname, f"{op} {r}"))

    with open(OUTFILE, "w") as f:
        f.write("\n".join(exports))
        f.write("\n\nsection .text\n\n")
        f.write("\n".join(functions))

    return


if __name__ == "__main__":
    main()
