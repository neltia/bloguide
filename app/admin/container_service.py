def get_container_list():
    return {"containers": ["container1", "container2"]}


def get_container(container_id):
    if container_id not in ["container1", "container2"]:
        return None
    return {"container_id": container_id}


def create_or_restart_container(container_id):
    return {"message": f"Container {container_id} created or restarted"}


def delete_container(container_id):
    return {"message": f"Container {container_id} deleted"}
