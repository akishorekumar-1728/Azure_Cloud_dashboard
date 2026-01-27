from app import compute_client

print("Connecting to Azure...")

for vm in compute_client.virtual_machines.list_all():
    print(vm.name)

print("SUCCESS ✅")
