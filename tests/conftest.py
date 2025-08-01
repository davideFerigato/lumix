import pytest

@pytest.fixture(autouse=True)
def configure_environment(monkeypatch):
    """
    Fixture eseguita automaticamente prima di ogni test.
    Può essere usata per configurare variabili d'ambiente o mocking globale.
    """
    monkeypatch.setenv("LUMIX_ENV", "test")
