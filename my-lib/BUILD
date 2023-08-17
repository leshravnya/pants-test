resource(name="pyproject", source="pyproject.toml")

python_distribution(
    name="my-lib",
    dependencies=[
        ":pyproject",
        "my-lib/src:src",
        "my-lib/src/libv:libv",
        "my-lib/src/libv/utils:utils"
        # Dependencies on code to be packaged into the distribution.
    ],
    provides=python_artifact(
        name="my-lib",
        version="0.0.1"
    ),
    # Example of setuptools config, other build backends may have other config.
    wheel_config_settings={"--global-option": ["--python-tag", "py38,py39,py310"]},
    generate_setup=True,
)
