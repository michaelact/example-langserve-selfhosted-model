# langserve_launch_example

<!--- This is a LangChain project bootstrapped by [LangChain CLI](https://github.com/langchain-ai/langchain). --->

## Customise

To customise this project, edit the following files:

- `langserve_launch_example/chain.py` contains an example chain, which you can edit to suit your needs.
- `langserve_launch_example/server.py` contains a FastAPI app that serves that chain using `langserve`. You can edit this to add more endpoints or customise your server.
- `tests/test_chain.py` contains tests for the chain. You can edit this to add more tests.
- `pyproject.toml` contains the project metadata, including the project name, version, and dependencies. You can edit this to add more dependencies or customise your project metadata.

## Install dependencies

If using poetry:

```bash
poetry install
```

If using vanilla pip:

```bash
pip install .
```

## Usage

You will need to set environment variables, by creating `.env` file which contains:

```
HUGGINGFACEHUB_API_TOKEN="hf_..."
HUGGINGFACEHUB_REPO_ID="user/repo"
```

To run the project locally, run

```
docker compose up
```

This will launch a webserver on port 8001.

## Contributing

For information on how to set up your dev environment and contribute, see [here](.github/CONTRIBUTING.md).
