from packets import PackTime  # Replace 'your_module' with the actual module name
import alerts_manager

if __name__ == "__main__":
    pack_time = PackTime()
    pack_time.run_sniffer()
    getter = alerts_manager.AlertManager().sharedAlerts
    print("here")
    print(getter)

