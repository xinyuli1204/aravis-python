## Aravis python Binding

### Usage
```
import aravis
from aravis import Aravis
Aravis.update_device_list()
connected_num_device = Aravis.get_n_devices()
print("Device number: {} ".format(connected_num_device))
```
