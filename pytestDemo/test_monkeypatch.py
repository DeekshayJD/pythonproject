import my_module

def test_my_function(monkeypatch):
    def mock_function():
        return "mocked result"

    monkeypatch.setattr("my_module_path.my_function", mock_function)
    assert my_module.my_function() == "mocked result"
