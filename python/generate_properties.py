from string import Template
try:
    import vim
except: 
    pass

template = Template("""private ${primitive}Property${generic} ${name} = new Simple${primitive}Property${brackets}(this, "${name}");
public ${primitive}Property${generic} ${name}Property() {return this.${name};}
public ${get_and_set_type} get${big_name}() {return this.${name}.get();}
public void set${big_name}(${get_and_set_type} ${name}) {this.${name}.set(${name});}""")


def generate_property(primitive, name, obj_type):
    get_and_set_type = primitive
    brackets = ""
    generic = ""

    if obj_type:
        brackets = "<>"
        generic = "<{}>".format(obj_type)
    if primitive in ["List", "Map", "Set"]:
        brackets = "<>"
        get_and_set_type = "Observable{}{}".format(primitive, generic)

    elif primitive == "Object":
        get_and_set_type = obj_type
    else:
        obj_type = ""

    big_name = name[0].upper() + name[1:]

    output = template.substitute(primitive=primitive,
                                 name=name,
                                 big_name=big_name,
                                 generic=generic,
                                 get_and_set_type=get_and_set_type,
                                 brackets=brackets)

    return output

def gen_prop(args):
    if len(args) not in [2, 3]:
        print("Usage: :GenProp PropertyType name [ElementType]")
        return
    
    primitive = args[0]
    name = args[1]
    obj_type = ""
    if len(args) == 3:
        obj_type = args[2]

    prop = generate_property(primitive, name, obj_type).split("\n")
    
    b = vim.current.buffer
    (row, col) = vim.current.window.cursor

    row = row -1
    b[row:row] = prop
    
