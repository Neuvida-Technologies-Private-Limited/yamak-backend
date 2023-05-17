from access.models import User
from workspace.models import Experiment, Workspace
from main.mixins.exceptions import UnAuthorizedError

def create_experiment(user: User, workspace_id: str, name: str) -> None:
    """
    Create the experiment in the workspace
    """

    # check workspace
    workspace = Workspace.objects.filter(workspace_id=workspace_id, created_by=user).last()
    
    if not workspace:
        raise UnAuthorizedError('invalid user/workspace')

    Experiment.objects.create(workspace=workspace, name=name)

    return

def edit_experiment(user: User, workspace_id: str, experiment_id: str, name: str) -> None:
    """
    Create the experiment in the workspace
    """

    # check workspace
    workspace = Workspace.objects.filter(workspace_id=workspace_id, created_by=user).values()

    if not workspace:
        raise UnAuthorizedError('invalid workspace_id')

    # workspace primary key    
    workspace_id_pk = list(workspace)[0]['id'] 

    # check experiment
    experiment = Experiment.objects.filter(experiment_id=experiment_id, workspace_id=workspace_id_pk)

    if not experiment:
        raise UnAuthorizedError('invalid experiment_id')
    
    # delete experiment
    experiment.update(name=name)

    return

def delete_experiment(user: User, workspace_id: str, experiment_id: str) -> None:
    """
    Create the experiment in the workspace
    """

    # check workspace
    workspace = Workspace.objects.filter(workspace_id=workspace_id, created_by=user).values()

    if not workspace:
        raise UnAuthorizedError('invalid workspace_id')

    # workspace primary key    
    workspace_id_pk = list(workspace)[0]['id'] 

    # check experiment
    experiment = Experiment.objects.filter(experiment_id=experiment_id, workspace_id=workspace_id_pk)

    if not experiment:
        raise UnAuthorizedError('invalid experiment_id')
    
    # update experiment
    experiment.delete()

    return

