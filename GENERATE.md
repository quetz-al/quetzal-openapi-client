Auto-generation instructions
============================

1. Set environment variables:
    ```
    export GIT_USER_ID=quetz-al
    export GIT_REPO_ID=quetzal-openapi-client
    ```
2. Run auto-generator script `./generate.sh`.
3. Review changes with `git status`.  Take special care of the following files,
   which have already caused problems in the past:

   * The `.gitignore` file, which is rewritten by the auto-generator.
   * The `setup.py`, which should have the `namespace_packages=['quetzal']`
     keyword parameter. Also, the `VERSION` variable needs to be
     **changed manually**.
4. (Optional, can be done manually). Commit/push changes with 
   `./git_push.sh $GIT_USER_ID $GIT_REPO_ID "<your commit message>"`
5. (Optional, can be done manually through github) tag a release and push the 
   tag. Use `v` as a prefix:
    ```
    git tag -a vX.Y.Z -m "<Some meaningful tag message>"
    git push --tags
    ```
6. (Optional) Build and push a new package to PyPI test first:

    ```
    rm -rf dist
    python setup.py sdist bdist_wheel
    python -m twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/*
    ```
   
   Then, after verifying that this worked correctly, upload to the real PyPI
   servers:
   
   ```
   python -m twine upload dist/*
   ```
