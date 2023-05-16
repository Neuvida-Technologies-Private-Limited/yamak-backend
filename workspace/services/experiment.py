from access.models import User
from workspace.models import Experiment
from main.mixins.exceptions import UnAuthorizedError

def get_experiment(user: User, id: str, name: str) -> None:
    """
    Create the workspace for the user
    """

    # create workspace
    workspace = Workspace.objects.filter(workspace_id=id, created_by=user)
    
    if not workspace:
        raise UnAuthorizedError('invalid user/workspace')

    # update workspace
    workspace.update(name=name)
    
    return
    
def create_experiment(user: User, name: str) -> None:
    """
    Create the workspace for the user
    """

    # create workspace
    Workspace.objects.create(name=name, created_by=user)

    return

def edit_experiment(user: User, id: str, name: str) -> None:
    """
    Create the workspace for the user
    """

    # create workspace
    workspace = Workspace.objects.filter(workspace_id=id, created_by=user)
    
    if not workspace:
        raise UnAuthorizedError('invalid user/workspace')

    # update workspace
    workspace.update(name=name)
    
    return

def delete_experiment(user: User, id: str) -> None:
    """
    Create the workspace for the user
    """

    # create workspace
    workspace = Workspace.objects.filter(workspace_id=id, created_by=user)

    if not workspace:
        raise UnAuthorizedError('invalid user/workspace')

    # delete workspace
    workspace.delete()

    return
