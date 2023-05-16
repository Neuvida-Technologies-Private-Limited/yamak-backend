from access.models import User
from workspace.models import Workspace
from main.mixins.exceptions import UnAuthorizedError

def create_workspace(user: User, name: str) -> None:
    """
    Create the workspace for the user
    """

    # create workspace
    Workspace.objects.create(name=name, created_by=user)

    return

def get_workspace(user: User) -> None:
    """
    Create the workspace for the user
    """

    # get workspace
    workspace_list = Workspace.objects.create(created_by=user).values()

    return workspace_list

def edit_workspace(user: User, id: str, name: str) -> None:
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

def delete_workspace(user: User, id: str) -> None:
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

# def share_workspace(user: User, id: str) -> None:
#     """
#     Create the workspace for the user
#     """

#     # create workspace
#     workspace = Workspace.objects.filter(workspace_id=id, created_by=user)

#     if not workspace:
#         raise UnAuthorizedError('invalid user/workspace')

#     # delete workspace
#     workspace.delete()

#     return