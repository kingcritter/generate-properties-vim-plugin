try:
    import vim
except: 
    pass

template = """private ###primitive###Property###type### ###name### = new Simple###primitive###Property###brackets###(this, "###name###");
public ###primitive###Property###type### ###name###Property() {return this.###name###;}
public ###interact_primitive######type### get###bigName###() {return this.###name###.get();}
public void set###bigName###(###interact_primitive######type### ###name###) {this.###name###.set(###name###);}"""


def generate_property(primitive, name, obj_type=""):
    interact_primitive = primitive
    brackets = ""
    
    if obj_type:
        obj_type = "<" + obj_type + ">"
        primitive_or_type = obj_type
        brackets = "<>"

    if primitive == "List":
        interact_primitive = "ObservableList"

    bigName = name[0].upper() + name[1:]

    output = template.replace("###primitive###", primitive)
    output = output.replace("###name###", name)
    output = output.replace("###bigName###", bigName)
    output = output.replace("###type###", obj_type)
    output = output.replace("###interact_primitive###", interact_primitive)
    output = output.replace("###brackets###", brackets)

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
    
