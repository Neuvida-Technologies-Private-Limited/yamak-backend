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

def get_workspace_info(user: User) -> None:
    """
    Create the workspace for the user
    """

    # get workspace
    workspace_list = list(Workspace.objects.filter(created_by=user).values('workspace_id', 'name', 'created_at', 'modified_at'))
    print('****', workspace_list, '****')

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