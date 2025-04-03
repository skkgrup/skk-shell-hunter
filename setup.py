from setuptools import setup, find_packages

setup(
    name="skk-shell-hunter",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "skk-hunter=skk_shell_hunter:StealthShellHunter"
        ]
    },
    author="SKK Group",
    description="A shell scanner tool for security testing.",
    url="https://github.com/skkgrup/skk-shell-hunter",
)
