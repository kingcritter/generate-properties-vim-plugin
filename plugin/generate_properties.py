template = """private ###primitive###Property###type### ###name### = new Simple###primitive###Property###brackets###(this, "###name###");
public ###primitive###Property###type### ###name###Property() {return this.###name###}
public ###interact_primitive######type### get###bigName###() {return this.###name###.get();}
public void set###bigName###(###interact_primitive######type### ###name###) {this.###name###.set(###name###);}"""


def generate_property(primitive, name, obj_type=""):
    primitive = primitive.capitalize()
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

def print_hello():
    print("hello!")

#while True:
#    args = raw_input(">>> ")
#    args = args.split(" ")
#    
#    if len(args) == 2:
#        x = generate_property(args[0], args[1])
#    elif len(args) == 3:
        x = generate_property(args[0], args[1], args[2])

    print(x)