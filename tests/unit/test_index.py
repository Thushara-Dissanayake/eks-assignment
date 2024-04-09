import pytest
import eks_assignment.lambda_handler.index as index

def env(env: str):
    if env == "dev":
        def mock_get_ssm_parameters():
            return "development"
    elif env == "staging":
        def mock_get_ssm_parameters():
            return "staging"
    else:
        def mock_get_ssm_parameters():
            return "production"

    return mock_get_ssm_parameters

@pytest.fixture()
def return_param_dev(monkeypatch):
    monkeypatch.setattr(index, "get_ssm_parameters", env("dev"))

@pytest.fixture()
def return_param_prod(monkeypatch):
    monkeypatch.setattr(index, "get_ssm_parameters", env("staging"))

@pytest.fixture()
def return_param_staging(monkeypatch):
    monkeypatch.setattr(index, "get_ssm_parameters", env("production"))

def test_handler_returns_correct_replica_count_for_dev(return_param_dev):
    result = index.handler(event={}, context={})
    assert result["Data"]["ReplicaCount"] == 1

def test_handler_returns_correct_replica_count_for_staging(return_param_staging):
    result = index.handler(event={}, context={})
    assert result["Data"]["ReplicaCount"] == 2

def test_handler_returns_correct_replica_count_for_prod(return_param_prod):
    result = index.handler(event={}, context={})
    assert result["Data"]["ReplicaCount"] == 2
