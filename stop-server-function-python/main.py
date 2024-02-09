from googleapiclient import discovery

def StopVM(request):
    # Stop the VM
    service = discovery.build('compute', 'v1')
    result = service.instances().stop(project='GCP_PROJECT', zone='GCP_ZONE', instance='minecraft-server').execute()
    return "Server stopped"
