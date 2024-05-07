from aravis import Aravis
Aravis.update_device_list()
connected_num_device = Aravis.get_n_devices()
if connected_num_device == 0:
    Aravis.shutdown()
    print("No device was found.")
else:
    print("Device number: {} ".format(connected_num_device))
