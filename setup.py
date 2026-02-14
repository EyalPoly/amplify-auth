from setuptools import setup, find_packages

setup(
    name="amplify-auth",
    version="0.1.0",
    author="Eyal Politansky",
    author_email="10eyal10@gmail.com",
    description="Shared authentication providers for Amplify projects",
    url="https://github.com/EyalPoly/amplify-auth",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "boto3>=1.18.0",
        "pycognito>=2023.5.0",
        "PyJWT>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "mypy>=1.8.0",
            "black>=24.1.0",
        ],
    },
)