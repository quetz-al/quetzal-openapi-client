#!/bin/bash

set -e

QUETZAL_URL="https://quetz.al/api/v1/openapi.json"
WORK_DIR=$(mktemp -d /tmp/quetzal-client-generator.XXXXXX)

# Generate with a docker image of the openapi-generator-cli project, or with a
# local clone of this repo. Until recently, we were using the former, but some
# particular regressions impact us and there has not been a release yet. The
# regression is documented here:
# https://github.com/OpenAPITools/openapi-generator/issues/2209
#
# For this case, set this variable:
OPENAPI_GENERATOR_CLI_DIR=${HOME}/apps/openapi-generator


# For an official openapi-generator-cli Docker image, use this variable instead:
# DOCKER_IMAGE="openapitools/openapi-generator-cli:v4.0.0-beta2"

if [[ -z ${DOCKER_IMAGE} ]]
then
   # When DOCKER_IMAGE is not defined or is empty
   if [[ -d ${OPENAPI_GENERATOR_CLI_DIR} ]]
   then
       pushd ${OPENAPI_GENERATOR_CLI_DIR}
       REFERENCE="git-$(git rev-parse --short HEAD)"
       popd
       echo "Using local openapi-generator-cli in ${OPENAPI_GENERATOR_CLI_DIR}."
       echo "Generator reference is ${REFERENCE}..."
   else
       echo "${OPENAPI_GENERATOR_CLI_DIR} not defined."
       exit -1
   fi
   GENERATE_CMD="java -jar ${OPENAPI_GENERATOR_CLI_DIR}/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate"

else
    echo "Pulling docker image..."
    docker image pull ${DOCKER_IMAGE}
    REFERENCE="docker-$(docker image inspect --format "{{.Id}}" ${DOCKER_IMAGE})"
    GENERATE_CMD="docker run --rm -v ${PWD}:${PWD} -v ${WORK_DIR}:${WORK_DIR}:ro ${DOCKER_IMAGE} generate"
fi
echo "Generator reference is ${REFERENCE}."

echo "Downloading API specification..."
curl --insecure -o ${WORK_DIR}/openapi.json ${QUETZAL_URL}

# Fix the $refs, which generate incorrect code as shown in
# https://github.com/OpenAPITools/openapi-generator/issues/1991
echo "Dereferencing..."
python deref.py ${WORK_DIR}/openapi.json ${WORK_DIR}/openapi-noref.json
cp openapi-generator-config.json ${WORK_DIR}


echo "Running openapi-generator-cli..."
${GENERATE_CMD} \
    -i ${WORK_DIR}/openapi-noref.json \
    -g python \
    -c ${WORK_DIR}/openapi-generator-config.json \
    -o ${PWD}

echo "Saving reference..."
cat >> quetzal/openapi_client/__init__.py <<EOF

# Added by generate.sh:
# Add a complete reference to the generator version:
# a git commit or Docker image ID used to generate this code with openapi-generator-cli
__openapi_generator_cli_version__ = "${REFERENCE}"
EOF

echo "Fixing README.md..."
if [[ -z ${GIT_REPO_ID} ]]
then
    echo "GIT_REPO_ID not defined, README.md will have some weird references."
else
    sed -i '' -e 's/GIT_REPO_ID/'"$GIT_REPO_ID"'/g' ./README.md
fi

if [[ -z ${GIT_USER_ID} ]]
then
    echo "GIT_USER_ID not defined, README.md will have some weird references."
else
    sed -i '' -e 's/GIT_USER_ID/'"$GIT_USER_ID"'/g' ./README.md
fi

# echo "Fixing documentation..."
# mkdir -p docs/sphinx/source/autogen

# echo "Converting README.md -> docs/sphinx/source/autogen/README.rst"
# #sed -e "s/docs\/(\(.*\).md/\1/g" < README.md | 
# #sed -e "s/(docs\/.*\.md\#\(.*\))/(\1)/g" < README.md | 
# sed -e "s/(docs\/\(.*\).md)/(\1.html)/g" < README.md | \
#     sed -e "s/(docs\/\(.*\).md\#\(.*\))/(\1.html\#\2)/g" | \
#     pandoc --to=rst --base-header-level=2 --columns 1000 --output docs/sphinx/source/autogen/README.rst

# for filename in docs/*.md
# do
#     rst_filename="docs/sphinx/source/autogen/$(basename ${filename} .md).rst"
#     echo "Converting ${filename} -> ${rst_filename}"
#     #sed -e "s/(\(.*\).md/\1/g" < ${filename} | \
#     pandoc --to=rst --base-header-level=2 --columns 1000 --output ${rst_filename} < ${filename}
# done

