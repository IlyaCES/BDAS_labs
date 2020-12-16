from xml.etree import ElementTree as Et
import sys


source = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 `~!@#$%^*()_-+={[}]:;\"',.?\\|<>/"""
target = """>en@U#(rfPTY"h,Xl=3}Qx-54W9Dz1$:B^omA.O)k\'F2KLc8G%|R{*~?piCj_qHZ0` aIg!vyVE[/+M]7JNuw6\\<b;tSsd"""
src_to_trg = dict(zip(source, target))
trg_to_src = dict(zip(target, source))


def obfuscate(string:str):
    return ''.join(map(lambda x: src_to_trg[x], string))


def deobfuscate(string:str):
    return ''.join(map(lambda x: trg_to_src[x], string))


def change_xml(tree, f):
    for element in tree.iter():
      if (not element.text.isspace()):
          element.text = f(element.text)
      element.attrib = {k: f(v) for k, v in element.attrib.items()}


def main():
    args = sys.argv[1:]
    
    if not len(args):
        sys.exit("Not enough args")

    if args[0] == '-d':
      f = deobfuscate
      args = args[1:]
    else:
      f = obfuscate
    
    in_file_name = args[0]
    out_file_name = args[1] if len(args) >= 2 else 'obfuscator_result.xml'
    
    tree = Et.parse(in_file_name)
    
    change_xml(tree, f)
    
    tree.write(out_file_name)


if __name__ == '__main__':
  main()
