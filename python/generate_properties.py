from string import Template
try:
    import vim
except: 
    pass

template = Template("""private ${_primitive}Property${_obj_type} ${_name} = new Simple${_primitive}Property${_brackets}(this, "${_name}");
public ${_primitive}Property${_obj_type} ${_name}Property() {return this.${_name};}
public ${_get_and_set_type}${_obj_type} get${_big_name}() {return this.${_name}.get();}
public void set${_big_name}(${_get_and_set_type}${_obj_type} ${_name}) {this.${_name}.set(${_name});}""")


def generate_property(primitive, name, obj_type=""):
    get_and_set_type = primitive
    brackets = ""
    
    if obj_type:
        obj_type = "<" + obj_type + ">"
        primitive_or_type = obj_type
        brackets = "<>"

    if primitive in ["List", "Map", "Set"]:
        get_and_set_type = "Observable" + primitive

    big_name = name[0].upper() + name[1:]

    output = template.substitute(_primitive=primitive,
                                 _name=name,
                                 _big_name=big_name,
                                 _obj_type=obj_type,
                                 _get_and_set_type=get_and_set_type,
                                 _brackets=brackets)

    return output

def gen_prop(args):
    if len(args) not in [2, 3]:
        print("Not enough arguments!")
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
    
