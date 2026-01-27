from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

SUBSCRIPTION_ID = AZURE_SUBSCRIPTION_ID

credential = ClientSecretCredential(
    tenant_id=AZURE_TENANT_ID,
    client_id=AZURE_CLIENT_ID,
    client_secret=AZURE_CLIENT_SECRET
)

compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)

print("Connecting to Azure...")

for vm in compute_client.virtual_machines.list_all():
    print("VM Name:", vm.name)
