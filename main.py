from IPython.terminal.ipapp import launch_new_instance
from IPython.lib import passwd
from socket import gethostname
import sys
import warnings
warnings.filterwarnings("ignore", module = "zmq.*")
sys.argv.append("notebook")
sys.argv.append("--IPKernelApp.pylab='inline'")
sys.argv.append("--NotebookApp.ip=" + gethostname())
sys.argv.append("--NotebookApp.open_browser=False")
sys.argv.append("--NotebookApp.password=''" )
r = launch_new_instance()
print(f"***********************************************{r}")