from translate import Translator


def concat(*args, sep=" "):
    return sep.join(args)


translator = Translator(to_lang="ru")
f_name_in = input("Enter name input text file:\n")
f_name_out = input("Enter name output text file:\n")
sep = "-"
txt_file_out = open(f_name_out, "w")
try:
    with open(f_name_in, 'r') as txt_file_in:
        for line in txt_file_in:
            txt_file_out.write(concat(translator.translate(line.split(sep)[0]), line.split(sep)[1], sep=sep))
except IOError:
    print(r"input\output error!")
finally:
    txt_file_out.close()
