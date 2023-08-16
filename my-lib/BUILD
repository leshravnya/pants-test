resource(name="pyproject", source="pyproject.toml")
python_sources(name="lib", sources=["lib/**/*.py"])

python_distribution(
    name="my-lib",
    dependencies=[
        ":pyproject",
        ":lib"
        # Dependencies on code to be packaged into the distribution.
    ],
    provides=python_artifact(
        name="my-lib",
        version="0.0.1"
    ),
    # Example of setuptools config, other build backends may have other config.
    wheel_config_settings={"--global-option": ["--python-tag", "py39"]},
    generate_setup=True,
)
