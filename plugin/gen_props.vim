if !has('python')
    echo "Error: vim not compiled with python support"
    finish
endif

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import generate_properties as gp
EOF

function! GenProp(...)
    python gp.gen_prop(vim.eval("a:000"))
endfunction

command -nargs=+ GenProp call GenProp(<f-args>)
